import os
import pyjsonrpc
import traceback

from tools import SimpleResponse, URLLoader
from commands import CommandRequestHandler, external_jsonrpc_command, commandline
from fetcher import Fetcher
from plutonium.plugins.plugin_manager import PluginManager, PluginLoader
from orm.manager import Manager

"""
    The handler class of the core Plutonium

    commands: cleanup!

"""

from plutonium.modules.logger import get_logger
logger = get_logger(__name__)

class Plutonium(object):

    def __init__(self, config):
        self.config = config
        self.url_loader = URLLoader()
        self.init_callbacks = []

    @external_jsonrpc_command
    @commandline('Database related commands', dict(command = dict(help='Command', type = str, choices = ['upgrade', 'clean'])))
    def database(self, command):
        if command == 'upgrade':
            try:
                from alembic.config import Config
                from alembic import command

                db_uri = self.config.data['database']['url'].value

                alembic_cfg = Config()
                alembic_cfg.set_main_option('script_location', os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'alembic')))
                alembic_cfg.set_main_option('sqlalchemy.url', db_uri)

                res = command.upgrade(alembic_cfg, "head")

                self.fetcher.reload()

                return SimpleResponse(True, "Upgrade is successful")

            except Exception as e:
                logger.exception(e)
                return SimpleResponse(False, str(e))

        elif command == 'clean':
            pass

        return SimpleResponse(True)

    # initialize all of the required stuffs for the Plutonium core
    @external_jsonrpc_command
    def init(self):
        try:
            # init plugins
            self.plugin_manager = PluginManager(PluginLoader('plugins', self))
            self.plugin_manager.load(self.config.data['plugins'])

        except Exception as e:
            logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during the plugin initalization: ' + str(e))

        try:
            # import orm related manager
            self.orm_manager = Manager(self.config.data)

        except Exception as e:
            logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during the database initalization: ' + str(e))

        try:
            self.fetcher = Fetcher(self.config, self.orm_manager, self.plugin_manager)
            self.fetcher.init_models()
            self.fetcher.fetch_feeds_from_database()
            self.fetcher.start()
            CommandRequestHandler.externals.append(self.fetcher)

        except Exception as e:
            logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during the fetcher initalization: ' + str(e))

        for callback in self.init_callbacks:
            try:
                callback()
            except Exception as e:
                logger.error(traceback.format_exc())
                return SimpleResponse(False, 'Exception occured during calling the init callback:' + str(e))

        return SimpleResponse(True)

    def register_after_successfully_init(self, callback):
        self.init_callbacks.append(callback)

    # Initialize the command server to receive IPC commands.
    def start_command_server(self):
        try:
            command_server_address = self.config.data['command_server']
            self.command_server = pyjsonrpc.ThreadingHttpServer(
                server_address = (command_server_address['host'].value, command_server_address['port'].value),
                RequestHandlerClass = CommandRequestHandler
            )
        except Exception as e:
            logger.error('Exception occured during the command server initalization: ' + str(e) + traceback.format_exc())
            return

        CommandRequestHandler.externals.append(self)

        self.command_server.serve_forever()

    @external_jsonrpc_command
    @commandline('Reload the config')
    def reload(self):
        try:
            self.config.reload()
        except Exception as e:
            logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during config parsing: ' + str(e))

        return SimpleResponse(True)

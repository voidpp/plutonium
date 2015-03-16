import os
import pyjsonrpc
import traceback

from tools import SimpleResponse, URLLoader
from commands import CommandRequestHandler, external_jsonrpc_command, commandline
from fetcher import Fetcher
from plugins.plugin_manager import PluginManager, PluginLoader
from orm.manager import Manager

"""
    The handler class of the core Plutonium

    commands: cleanup!

"""
class Plutonium(object):

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.url_loader = URLLoader()
        self.init_callbacks = []

    # initialize all of the required stuffs for the Plutonium core
    @external_jsonrpc_command
    def init(self):
        try:
            # init plugins
            self.plugin_manager = PluginManager(PluginLoader('plugins', self), self.logger)
            self.plugin_manager.load(self.config.data['plugins'])

        except Exception as e:
            self.logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during the plugin initalization: ' + str(e))

        try:
            # import orm related manager
            self.orm_manager = Manager(self.config.data, self.logger)

            self.orm_manager.decorate_models(self.url_loader)

        except Exception as e:
            self.logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during the database initalization: ' + str(e))

        try:
            self.fetcher = Fetcher(self.config, self.logger, self.orm_manager, self.plugin_manager)
            self.fetcher.init_models()
            self.fetcher.fetch_feeds_from_database()
            self.fetcher.start()
            CommandRequestHandler.externals.append(self.fetcher)

        except Exception as e:
            self.logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during the fetcher initalization: ' + str(e))

        for callback in self.init_callbacks:
            try:
                callback()
            except Exception as e:
                self.logger.error(traceback.format_exc())
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
            self.logger.error('Exception occured during the command server initalization: ' + str(e) + traceback.format_exc())
            return

        CommandRequestHandler.logger = self.logger
        CommandRequestHandler.externals.append(self)

        self.command_server.serve_forever()

    @external_jsonrpc_command
    @commandline('Reload the config')
    def reload(self):
        try:
            self.config.reload()
        except Exception as e:
            self.logger.error(traceback.format_exc())
            return SimpleResponse(False, 'Exception occured during config parsing: ' + str(e))

        return SimpleResponse(True)

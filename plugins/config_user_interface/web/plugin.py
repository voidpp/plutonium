from plugins.plugin import ConfigUserInterfacePluginBase

from http_server import AdvancedHTTPServer
from http_handler import RawHTTPHandler, VirtualHandler

import os
import threading

class WebConfigUserInterfacePlugin(ConfigUserInterfacePluginBase):

    def __init__(self, host, port, plutonium):
        self.host = host
        self.port = port
        self.httpd = None
        self.logger = plutonium.logger

        RawHTTPHandler.document_root = os.getcwd() + '/plugins/config_user_interface/web/wwwroot'
        RawHTTPHandler.file_not_found_handler = VirtualHandler()
        RawHTTPHandler.logger = plutonium.logger
        #RawHTTPHandler.file_not_found_handler.register('\/feeds.*', Feeds())

    def listen(self):
        address = (self.host, self.port)
        self.logger.info('Web UI server listen on %s:%d' % address)

        if self.httpd:
            self.httpd.shutdown()

        self.httpd = AdvancedHTTPServer(address, RawHTTPHandler, self.logger, 10)

        th = threading.Thread(target=self.httpd.serve_forever)
        th.setDaemon(True)
        th.start()

    def start(self):
        self.listen()

    def stop(self):
        self.logger.info('Web UI server is stopping...')
        if self.httpd:
            self.httpd.shutdown()

    def reload(self, host, port):
        self.stop()
        self.host = host
        self.port = port
        self.listen()


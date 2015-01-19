
import time
import urllib2
import pyjsonrpc

from tools import Storage, SimpleResponse
from background_process_handler import BackgroundProcessHandler

# used by the init script to manage the Plutonium process, eg start, stop creates the IPC interface
class PlutoniumManager(BackgroundProcessHandler):

    def __init__(self, control_port, pid_file, logger):
        super(PlutoniumManager, self).__init__(["python", "plutonium.py"], pid_file, logger)
        self.control_port = control_port

    def get_rpc_client(self):
        return pyjsonrpc.HttpClient(url = "http://localhost:%d/jsonrpc" % self.control_port)

    def start(self):
        result = super(PlutoniumManager, self).start()

        rpc_client = self.get_rpc_client()

        """
            The BackgroundProcessHandler.start function executes the plutonium script, and returns immediately.
            But the command server not available yet, so we need to wait for it.
        """
        attempts = 50

        while True:
            try:
                rpc_client.ping()
                break
            except urllib2.URLError as e:
                attempts = attempts - 1
                if attempts > 0:
                    time.sleep(0.1)
                else:
                    break

        if not attempts:
            # if the Plutonium process unwilling to communicate, needs to stop it!
            self.stop()
            return SimpleResponse(False, 'Initialize of Plutonium has been failed')

        init_res = Storage(rpc_client.init())

        self.logger.debug('Init plutonium: ' + str(init_res))

        if init_res.code:
            result.message = result.message + ' and initialized'

        return result

    def control(self, name, args = {}):

        self.logger.debug("Send rpc command '%s' with args: %s" % (name, args))

        rpc_client = self.get_rpc_client()
        func = getattr(rpc_client, name)

        response = func(**args)

        return SimpleResponse(**dict(response))

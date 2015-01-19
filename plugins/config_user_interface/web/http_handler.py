import SimpleHTTPServer

import os, re
from urlparse import urlparse, parse_qs
from abc import abstractmethod

class HTTPResponse(object):
    def __init__(self, content, code):
        self.content = content
        self.code = code


class RawHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    document_root = ''
    default_file = 'index.html'
    file_not_found_handler = None
    logger = None

    def log_message(self, format, *args):
        # called from parent class...
        self.logger.debug("HTTP request - %s - %s" % (self.client_address[0], format % args))

    def respond(self, response):
        self.send_response(response.code)
        self.send_header("Content-Length", str(len(response.content)))
        self.end_headers()
        self.wfile.write(response.content)

    def handle_all(self):
        request_path_parts = urlparse(self.path)

        request_path = request_path_parts.path

        # if request is domain.hu -> domain.hu/index.html
        if request_path.endswith('/'):
            request_path = request_path + self.default_file

        file_path = self.document_root + request_path

        # serve the file if exists
        if os.path.isfile(file_path):
            with open(file_path) as f:
                self.respond(f.read(), 200)
                return

        # if the requested file not exists call the "not found handler"
        if self.file_not_found_handler:
            result = self.file_not_found_handler.handle_request(request_path_parts)
            self.respond(HTTPResponse(result.content, result.code))
            return

        self.respond(HTTPResponse('file not found', 404))

    def do_GET(self):
        self.handle_all()

    def do_POST(self):
        self.handle_all()


"""
    Virtual requests:
        these are totally normal HTTP requests. If the uri not pointing to any file the request become virtual in this implementation
"""

# handle one request filtered by regex pattern
class VirtualRequestHandlerBase(object):

    @abstractmethod
    def handle(self, params, response, request):
        pass

# managing virtual requests
class VirtualHandler(object):

    def __init__(self):
        self.registered_paths = {}

    """
        pattern: regex pattern string
        handler: VirtualRequestHandlerBase inherited class instance
    """
    def register(self, pattern, handler):
        self.registered_paths[pattern] = handler

    def handle_request(self, request):
        params = parse_qs(request.query)

        for pattern in self.registered_paths:
            result = re.match(pattern, request.path)
            if result is not None:
                response = HTTPResponse('', 200)
                self.registered_paths[pattern].handle(params, response, request)
                return response

        return HTTPResponse('virtual request handler not found', 404)
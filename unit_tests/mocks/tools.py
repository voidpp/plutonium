
from modules.tools import URLLoader, HTTPResponse

class FakeURLLoader(URLLoader):
    def __init__(self, content = ''):
        self.content = ''

    def load(self, url):
        return HTTPResponse(200, self.content, {})
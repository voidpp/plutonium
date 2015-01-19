
from logging import Logger, NullHandler

class FakeLogger(Logger):

    def __init__(self, *args, **kwargs):
        self.messages = []
        super(FakeLogger, self).__init__(*args, **kwargs)

def get_logger():
    logger = FakeLogger(0)
    logger.addHandler(NullHandler(0))
    return logger

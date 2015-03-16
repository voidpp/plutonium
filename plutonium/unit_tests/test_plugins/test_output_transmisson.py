import unittest
from lxml import etree

from feed import Feed
from output import Output
from torrent import Torrent
from filter import Filter

from mocks.logger import FakeLogger

from plugins.output.transmission.plugin import TransmissionOutputPlugin

class TestSend(unittest.TestCase):
    def setUp(self):
        #self.output = TransmissionOutputPlugin(FakeLogger())
        pass

    def test_one(self):
        pass

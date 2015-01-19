import unittest
from lxml import etree

from feed import Feed
from output import Output
from torrent import Torrent
from filter import Filter

from rss_test_content import rss_test_content_head, rss_test_content_items, rss_test_content_foot
from mocks.tools import FakeURLLoader
from mocks.logger import get_logger
from mocks.fake_fetcher import FakeFetcher

class FakeOutputPlugin(object):
    def send(self, torrent):
        pass
    def get_required_params_struct(self):
        return dict()

Output.output_plugins = dict(
    transmission = FakeOutputPlugin()
)

class TestFetch(unittest.TestCase):
    def setUp(self):
        self.url_loader = FakeURLLoader()
        self.fetcher = FakeFetcher(0,0,0,0)
        Feed.__url_loader__ = self.url_loader
        Feed.__logger__ = get_logger()
        self.output = Output(name = 'trans1', type = 'transmission', params = '{}')
        self.feed = Feed(url = '', output = self.output, id = 0)
        self.feed.set_fetcher(self.fetcher)

    def get_xml_items(self, items):
        return rss_test_content_head + ''.join(items) + rss_test_content_foot

    def test_add_some_torrent_to_empty_feed(self):
        self.assertEqual(len(self.feed.torrents), 0)
        self.url_loader.content = self.get_xml_items(rss_test_content_items[-10:])
        self.feed.fetch()
        self.assertEqual(len(self.feed.torrents), 10)

    def test_add_some_torrent_to_non_empty_feed(self):
        self.assertEqual(len(self.feed.torrents), 0)
        self.url_loader.content = self.get_xml_items(rss_test_content_items[-10:])
        self.feed.fetch()
        self.assertEqual(len(self.feed.torrents), 10)
        self.url_loader.content = self.get_xml_items(rss_test_content_items[-15:])
        self.feed.fetch()
        self.assertEqual(len(self.feed.torrents), 15)

    def test_refetch_in_a_non_empty_feed(self):
        self.assertEqual(len(self.feed.torrents), 0)
        self.url_loader.content = self.get_xml_items(rss_test_content_items)
        self.feed.fetch()
        self.assertEqual(len(self.feed.torrents), 30)
        self.url_loader.content = self.get_xml_items(rss_test_content_items)
        self.feed.fetch()
        self.assertEqual(len(self.feed.torrents), 30)


class TestTorrentFiltering(unittest.TestCase):
    def setUp(self):
        self.feed = Feed()
        root = etree.Element("root")
        item = etree.SubElement(root, "item")
        self.item = item

    def add_required_xml_nodes(self):
        etree.SubElement(self.item, "guid").text = 'guid'
        etree.SubElement(self.item, "link").text = 'link'
        etree.SubElement(self.item, "title").text = 'title'

    def get_check_torrent(self):
        return Torrent(name = 'guid', title = 'title', link = 'link', is_sent_out = False)

    def test_without_link_node(self):
        self.assertEqual(self.feed.filter_torrent(self.item), None)

    def test_without_any_filter(self):
        self.add_required_xml_nodes()
        new_torrent = self.feed.filter_torrent(self.item)
        self.assertEqual(new_torrent, self.get_check_torrent())

    def test_without_non_matching_filters(self):
        self.add_required_xml_nodes()
        self.feed.filters.extend([Filter(source_node = 'title', pattern = 'k'), Filter(source_node = 'title', pattern = 'g')])
        new_torrent = self.feed.filter_torrent(self.item)
        self.assertEqual(new_torrent, self.get_check_torrent())

    def test_with_matching_filters(self):
        self.add_required_xml_nodes()
        self.feed.filters.append(Filter(source_node = 'title', pattern = 't.tle'))
        new_torrent = self.feed.filter_torrent(self.item)
        self.assertEqual(new_torrent, None)

    def test_with_matching_filters_with_mismatch_source_node(self):
        self.add_required_xml_nodes()
        self.feed.filters.append(Filter(source_node = 'guid', pattern = 't.tle'))
        new_torrent = self.feed.filter_torrent(self.item)
        self.assertEqual(new_torrent, self.get_check_torrent())

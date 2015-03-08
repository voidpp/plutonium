
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.relationships import RelationshipProperty
import re
from tools import xml_element_to_storage

from lxml import etree
from StringIO import StringIO

from orm.base import Base
from timer import Timer

from output import Output
from filter import Filter
from torrent import Torrent

feeds_filters_table = Table('feeds_filters', Base.metadata,
    Column('feed_id', Integer, ForeignKey('feeds.id')),
    Column('filter_id', Integer, ForeignKey('filters.id'))
)

class Feed(Base):
    __tablename__ = 'feeds'

    id = Column(Integer, primary_key = True)
    url = Column(Text)
    name = Column(Text)
    enabled = Column(Boolean)
    output_id = Column(Integer, ForeignKey("outputs.id"), nullable = False)
    update_interval = Column(Integer)
    last_update = Column(DateTime)
    target_path_pattern = Column(Text)
    filters = RelationshipProperty("Filter", secondary = feeds_filters_table)
    output = relationship("Output")
    #torrents: backref from Torrent model

    def min_str(self):
        return "<id: %(id)d, name: '%(name)s'>" % dict(self)

    def init_timer(self):
        if not hasattr(self, 'timer'):
            self.timer = Timer(self.update_interval, self.fetch)

    def set_fetcher(self, fetcher):
        self.__fetcher__ = fetcher
        return self

    def fetch(self):
        self.__logger__.debug("Start fetching feed " + self.min_str())
        feed_content = self.__url_loader__.load(self.url).content
        tree = etree.parse(StringIO(feed_content))

        output_handler = self.output.get_handler()

        if output_handler is None:
            self.__logger__.error("Not found output handler for feed '%s'" % self.name)
            return

        torrents = []

        for item in tree.xpath('/rss/channel/item'):
            guid = item.find('guid')

            if guid is None:
                self.__logger__.error("Not found guid in feed content for '%s'" % self.name)
                continue

            known = False

            # if this item is known, throw away
            for torrent in self.torrents:
                if torrent.name == guid.text:
                    known = True
                    break

            if known:
                continue

            new_torrent = self.filter_torrent(item)

            if not new_torrent:
                continue

            self.__logger__.debug("New torrent has been created in feed '%s'" % self.name)

            new_torrent.feed = self

            new_torrent.update_path_vars(xml_element_to_storage(item))

            new_torrent.is_sent_out = output_handler.send(new_torrent)

            torrents.append(new_torrent)

        if len(torrents):
            self.__fetcher__.add_torrents(torrents)

    def filter_torrent(self, torrent_xml_data):

        guid = torrent_xml_data.find('guid')
        link = torrent_xml_data.find('link')
        title_data = torrent_xml_data.find('title')
        title = '' if title_data is None else title_data.text

        if link is None:
            self.__logger__.error("Link node is missing from torrent xml node (%s)" % torrent_xml_data)
            return None

        filtered = False

        matches = None
        matched_source_node = None

        for filter in self.filters:
            source_node = torrent_xml_data.find(filter.source_node)
            if source_node is None:
                continue

            matches = re.match(filter.pattern, source_node.text)
            matched_source_node = filter.source_node

            if (matches is not None and filter.type == 'white') or (matches is None and filter.type == 'black'):
                filtered = True
                break

        if filtered:
            self.__logger__.debug("Torrent has been filtered. Filter: %s, Torrent: %s" % (filter.name, title))
            return None

        torrent = Torrent(name = guid.text, link = link.text, title = title, is_sent_out = False)

        # if there is no filters, matches is None
        if matches:
            path_vars = {}

            for idx, group in enumerate(matches.groups()):
                path_vars['%s:%d' % (matched_source_node, idx+1)] = group

            torrent.update_path_vars(path_vars)

        return torrent

    def start(self):
        self.__logger__.debug("Start fetching timer for feed " + self.min_str())
        self.init_timer()
        self.timer.start()

    def stop(self):
        self.__logger__.debug("Stop fetching timer for feed " + self.min_str())
        self.init_timer()
        self.timer.stop()

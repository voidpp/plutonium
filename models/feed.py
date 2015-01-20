
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.relationships import RelationshipProperty
import re

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

        new_items_cnt = 0

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

            new_torrent.is_sent_out = output_handler.send(new_torrent)

            self.__fetcher__.add_torrent(new_torrent)

            new_items_cnt += 1

        if new_items_cnt:
            self.__fetcher__.commit()

    def filter_torrent(self, torrent_xml_data):

        guid = torrent_xml_data.find('guid')
        link = torrent_xml_data.find('link')

        if link is None:
            self.__logger__.error("Link node is missing from torrent xml node (%s)" % torrent_xml_data)
            return None

        filtered = False

        for filter in self.filters:
            source_node = torrent_xml_data.find(filter.source_node)
            if source_node is None:
                continue

            if re.match(filter.pattern, source_node.text) is not None:
                filtered = True
                break

        if filtered:
            self.__logger__.debug("Torrent has been filtered. Filter: %s, Torrent: %s" % (filter, torrent_xml_data))
            return None

        title = torrent_xml_data.find('title')

        torrent = Torrent(name = guid.text, link = link.text, title = '' if title is None else title.text, is_sent_out = False)

        torrent._feed_item_data = torrent_xml_data

        return torrent

    def start(self):
        self.__logger__.debug("Start fetching timer for feed " + self.min_str())
        self.init_timer()
        self.timer.start()

    def stop(self):
        self.__logger__.debug("Stop fetching timer for feed " + self.min_str())
        self.init_timer()
        self.timer.stop()

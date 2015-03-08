
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
import datetime

from orm.base import Base

class Torrent(Base):
    __tablename__ = 'torrents'

    id = Column(Integer, primary_key = True)
    feed_id = Column(Integer, ForeignKey("feeds.id"), nullable = False)
    name = Column(String(length=255))
    title = Column(String(length=255))
    link = Column(String(length=255))
    is_sent_out = Column(Boolean)
    added = Column(DateTime, default=datetime.datetime.now)

    feed = relationship("Feed", backref = backref('torrents', order_by=id))


from sqlalchemy import Column, Integer, String, Enum

from orm.base import Base

class Filter(Base):
    __tablename__ = 'filters'

    id = Column(Integer, primary_key = True)
    name = Column(String(length=32))
    pattern = Column(String(length=64))
    source_node = Column(String(length=64))
    type = Column(Enum('black', 'white'), default = 'white')

import json
from sqlalchemy import Column, Integer, String, Text

from orm.base import Base
from orm.types import JSONEncoded

class Output(Base):
    __tablename__ = 'outputs'

    id = Column(Integer, primary_key = True)
    name = Column(String(length=32))
    type = Column(String(length=32))
    params = Column(JSONEncoded)
    """
    __parsed_params = None

    def get_params(self):

        if self.__parsed_params is not None:
            return self.__parsed_params

        try:
            self.__parsed_params = json.loads(self.params)
        except Exception as e:
            self.__logger__.critical("Cannot parse Output.params: '%s'. Reason: %s" % (self.params, e))

        return self.__parsed_params
    """
    def get_handler(self):
        if self.type not in self.output_plugins:
            self.__logger__.warning("Unknown output type '%s'" % self.type)
            return None

        handler = self.output_plugins[self.type]

        return handler

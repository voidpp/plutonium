
import os
import re
import sys
import importlib
import sqlalchemy
from sqlalchemy.orm import sessionmaker, scoped_session

from tools import ucfirst

class Manager(object):

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.factory = None

        self.__engine = None
        self.__session = None

    def __create_engine(self, echo = False):
        db_uri = self.config['database']['url'].value

        return sqlalchemy.create_engine(db_uri, echo = echo)

    def is_connected(self):
        if self.__engine is None:
            return False

        try:
            self.__engine.execute("SELECT 1")
        except:
            return False

        return True

    def get_engine(self):
        if not self.is_connected():
            self.__engine = self.__create_engine()

        return self.__engine

    def create_session(self):
        if self.__session:
            self.__session.close()

        session_factory = sessionmaker(bind=self.get_engine())
        session_class = scoped_session(session_factory)

        self.__session = session_class()
        return self.__session

    def decorate_models(self, url_loader):
        rx = re.compile('^([0-9a-z]{1,})\.py$')

        for file in os.listdir('models'):

            res = rx.match(file)
            if not res:
                continue

            module_name = res.group(1)
            class_name = ucfirst(module_name)

            # check of the module of the model has been already imported in this context
            if module_name in sys.modules:
                module = sys.modules[module_name]
            else:
                self.logger.debug("Loading model '%s'" % module_name)
                module = importlib.import_module('models.' + module_name)

            class_type = getattr(module, class_name)

            self.logger.debug("Decorating model '%s'" % class_name)

            if hasattr(class_type, '__need_logger__') and getattr(class_type, '__need_logger__'):
                setattr(class_type, '__logger__', self.logger)

            setattr(class_type, '__url_loader__', url_loader)

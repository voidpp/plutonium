
import os
import re
import sys
import importlib
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from tools import ucfirst
from sqlchemyforms.sqlchemyforms.form import as_form
from sqlchemyforms.sqlchemyforms.field import FieldFactory

class Manager(object):

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.engine = None
        self.factory = None

    def create_engine(self, echo = False):

        db_uri = self.config['database']['url'].value
        #encoding = self.config['database']['encoding'].value

        self.engine = sqlalchemy.create_engine(db_uri, echo = echo)

        return self.engine

    def create_session(self):
        Session = sessionmaker(bind=self.engine) #ez a param kell??
        Session.configure(bind=self.engine)

        self.session = Session()

        self.factory = FieldFactory(self.session)

        return self.session

    def decorate_models(self):
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

            if hasattr(class_type, '__need_form_factory__') and getattr(class_type, '__need_form_factory__'):
                setattr(class_type, '__factory__', self.factory)
                as_form(class_type)

            if hasattr(class_type, '__need_logger__') and getattr(class_type, '__need_logger__'):
                setattr(class_type, '__logger__', self.logger)


        # maybe this will be moved to some migration tools...
        self.logger.debug('Create tables: ' + str(class_type.metadata.tables.keys()))
        #class_type.metadata.drop_all(self.engine)
        class_type.metadata.create_all(self.engine)

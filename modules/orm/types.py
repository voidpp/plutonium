import json

from sqlalchemy.types import TypeDecorator
from sqlalchemy import Text

from utils import check_dict_struct

class JSONEncoded(TypeDecorator):

    impl = Text

    def __init__(self, struct = None):
        super(JSONEncoded, self).__init__()
        self.struct = struct

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is None:
            return value

        value = json.loads(value)

        if self.struct and not check_dict_struct(value, self.struct):
            return None

        return value



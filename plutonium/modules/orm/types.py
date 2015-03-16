import json

from sqlalchemy.types import TypeDecorator
from sqlalchemy import Text

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

def check_dict_struct(value, required):

	if type(value) is not dict or type(required) is not dict:
		return False

	def check_node(val_node, req_node):
		for key in req_node:
			if key not in val_node:
				return False

			if type(val_node[key]) is dict:
				if type(req_node[key]) is not dict:
					return False

				if not check_node(val_node[key], req_node[key]):
					return False

			elif type(val_node[key]) is not req_node[key]:
				return False

		return True

	return check_node(value, required)


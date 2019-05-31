import jsonschema.exceptions
from jsonschema.validators import Draft4Validator


# schema = {"items": {"type": "boolean"},  "minItems": 2}
# schema = {'format': 'date', 'type': 'string', 'maxLength': 10, 'pattern': '^[0-9]+'}


# validator = Draft7Validator(schema=schema)
# validator.validate('2019-05-01')
#
# validator.validate('2019/05/01')
# validator.validate('2019050100')
# validator.validate('2019年5月29日')
# validator.validate('2019-05')
# # validator.validate(201905)
# validator.validate('rlj00lsjf1')
schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "msg","email"
  ],
  "properties": {
    "msg": {
      "type": "string",
      "pattern": "^hello.*$"
    },
    "email": {
      "type": "string",
      "format": "email"
    }
  }
}
validator = Draft4Validator(schema=schema)
validator.validate({"msg": "hello,world", "email": 20})

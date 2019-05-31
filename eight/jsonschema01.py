# pip install jsonSchema
from jsonschema import validate

schema = {"type": "object", "properties": {"price": {"type": "number"}, "name": {"type": "string"}}}

validate(instance={"name":"Eggs","prince":"34.55"}, schema=schema)
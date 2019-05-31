from jsonschema import validate


schema = {"type": "object", "properties": {"price": {"type": "number"}, "name": {"type": "string"}}}
schema1 = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "name",
    "price"
  ],
  "properties": {
    "name": {
      "$id": "#/properties/name",
      "type": "string",
      "title": "The Name Schema",
      "default": "",
      "examples": [
        "Eggs"
      ],
      "pattern": "[A-Z]+"
    },
    "price": {
      "$id": "#/properties/price",
      "type": "number",
      "title": "The Price Schema",
      "default": 0.0,
      "examples": [
        34.99
      ]
    }
  }
}

# validate(instance={"name": "Eggs", "price": 34.99}, schema=schema)

validate(instance={"name": "Eggs", "price": "34.99"}, schema=schema)


import json
dict = {
  'message': 'success',
  'url': '',
  'data': {
    'address': '北京',
    'eid': 1,
    'name': '这是一个测试',
    'limit': 2000,
    'start_time': '2019-05-31T15:25:19',
    'status': True
  },
  'status': 200
}
# json = json.dumps(dict)
# print(json)

schema = {
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "message",
    "url",
    "data",
    "status"
  ],
  "properties": {
    "message": {
      "$id": "#/properties/message",
      "type": "string",
      "title": "The Message Schema",
      "enum": ["success", "error"],
      "pattern": "^(.*)$"
    },
    "url": {
      "$id": "#/properties/url",
      "type": "string",
      "title": "The url",
      "format": "uri",
    },
    "data": {
      "$id": "#/properties/data",
      "type": "object",
      "title": "The Data Schema",
      "required": [
        "address",
        "eid",
        "name",
        "limit",
        "start_time",
        "status"
      ],
      "properties": {
        "address": {
          "$id": "#/properties/data/properties/address",
          "type": "string",
          "title": "The Address Schema",
          "default": "",
          "examples": [
            "成都"
          ],
          "pattern": "^(.*)$"
        },
        "eid": {
          "$id": "#/properties/data/properties/eid",
          "type": "integer",
          "title": "The Eid Schema",
          "default": 0,
          "examples": [
            1
          ]
        },
        "name": {
          "$id": "#/properties/data/properties/name",
          "type": "string",
          "title": "The Name Schema",
          "default": "",
          "examples": [
            "这是也是汉字"
          ],
          "pattern": "^(.*)$"
        },
        "limit": {
          "$id": "#/properties/data/properties/limit",
          "type": "integer",
          "title": "The Limit Schema",
          "default": 0,
          "examples": [
            2000
          ]
        },
        "start_time": {
          "$id": "#/properties/data/properties/start_time",
          "type": "string",
          "title": "The Start_time Schema",
          "default": "",
          "format": "date-time",
          "examples": [
            "2017-11-21T15:25:19"
          ],
          "pattern": "^(.*)$"
        },
        "status": {
          "$id": "#/properties/data/properties/status",
          "type": "boolean",
          "title": "The Status Schema",
          "default": False,
          "examples": [
            True
          ]
        }
      }
    },
    "status": {
      "$id": "#/properties/status",
      "type": "integer",
      "title": "The Status Schema",
      "default": 0,
      "examples": [
        200
      ]
    }
  }
}

from jsonschema.validators import Draft4Validator


data = dict
validator = Draft4Validator(schema)
validator.validate(data)
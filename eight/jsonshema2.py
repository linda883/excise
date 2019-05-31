# from jsonschema import validate
# schema = {"items": {"type": "boolean"},  "minItems": 2}
# validate([True,False],schema=schema)


from jsonschema.validators import Draft4Validator


# schema = {"items": {"type": "boolean"},  "minItems": 2}
schema = {'format': 'date', 'type': 'string', 'maxLength': 10}
validator = Draft4Validator(schema=schema)
validator.validate('2019-05-01')
validator.validate('2019/05/01')
validator.validate('2019050100')
validator.validate('2019年5月29日')
validator.validate('2019-05sf')
validator.validate(2019050100000)
from jsonschema.validators import Draft4Validator

# 验证是否返回是html格式
schema = {
  "type": "string",
  "contentMediaType": "text/html"
}

v1 = Draft4Validator(schema=schema)
v1.validate('<!DOCTYPE html><html xmlns=\"http://www.w3.org/1999/xhtml\"><head></head></html>')

# 验证是加密的图片
schema1 = {
  "type": "string",
  "contentEncoding": "base64",
  "contentMediaType": "image/png"
}

v1 = Draft4Validator(schema=schema1)
v1.validate("iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAAA")

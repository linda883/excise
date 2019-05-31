import requests
import pytest
import json
from jsonschema.validators import Draft7Validator


def addviladator(respose_data):
    with open("schema2.json", 'r') as f:
        dict_schema = json.load(f)
    va = Draft7Validator(dict_schema)
    va.validate(respose_data)


def test_search_by_id():
    url = 'https://petstore.swagger.io/v2/pet/1'
    res = requests.get(url=url)
    respose_data = res.json()
    print(respose_data)
    assert res.status_code == 200
    assert respose_data['name'] == '9YZQCGVJM8'
    assert res.elapsed.total_seconds() <= 3
    addviladator(respose_data)


if __name__ == '__main__':
    pytest.main(['-s', 'test_swaggeruidemo6.py'])

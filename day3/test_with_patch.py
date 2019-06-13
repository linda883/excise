from MockExciseClass import ProductionClass
from unittest.mock import patch


def some_function():
    instance = ProductionClass.method()
    return instance.method()


with patch('MockExciseClass.ProductionClass.method') as mock:
    instance = mock.return_value
    instance.method.return_value = 'the result'
    result = some_function()
    assert result == 'the resultS'

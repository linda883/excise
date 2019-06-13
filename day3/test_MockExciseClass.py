from day3.MockExciseClass import ProductionClass
from unittest.mock import MagicMock,Mock

# real = ProductionClass()
# real.method = MagicMock(name='method')
# # real.something = MagicMock()
# real.method()
# print(real.method.assert_called_once_with())
# mock = Mock()
# real.closer(mock)
# print(mock.mock_calls)
# mock.close.assert_called_with()

# mock = Mock(return_value=3)
# mock.x =5
# print(mock())
# mock.return_value = 3
# print(mock())
# mock.something.return_value = 3
# print(mock.something())

mock = MagicMock()
print(mock.method())
print(mock.attribute.method(10, x=53))
print(mock.mock_calls)
print(mock.attribute.method.assert_called_with(10))
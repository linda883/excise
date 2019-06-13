
from unittest.mock import Mock

naf =Mock()
# print(naf())
# print(naf().method_any_method())
# print(naf.url)
# naf.return_value=18
# print(naf())
# naf.url.return_value="www.baidu.com"
# print(naf.url())
# naf.request.return_value={'name':'linda','age':18}
print(naf.request())
m=Mock()
# print(m(18))
# print(m(keyword='linda'))
print(m(18, keyword='linda'))
print(m(18, keyword='linda'))
# print(m.call_args_list)
# naf.request.side_effect=(200,404,302,500)

print(m.assert_called_once_with(18, keyword='linda'))








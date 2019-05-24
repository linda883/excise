import requests
import pytest
from ddt import ddt, file_data, unpack


@ddt
class TestMsg:

    @file_data('data.yaml')
    @unpack
    def test_post_get(self, **data):
        print(data)
        url = data.get('url')
        method = data.get('method')
        test_data = data.get('payload')
        message = data.get('validate')
        print(test_data, url, method)

        post_msg = requests.request(method=method, url=url, json=test_data)

        # print("code:"+str(post_msg.status_code))
        assert message.get('status_code') == post_msg.status_code
        print(post_msg.json())
        print("time:"+str(post_msg.elapsed.microseconds/1000)+"ms")


if __name__ == '__main__':
    pytest.main(['-s','test_request_demo.py'])

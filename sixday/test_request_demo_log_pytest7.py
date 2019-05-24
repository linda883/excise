import requests
import logging
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
        print(test_data, url, method)
        post_msg = requests.request(method=method, url=url, data=test_data)
        logging.info("code:"+str(post_msg.status_code))
        logging.info(post_msg.text)
        logging.info("time:"+str(post_msg.elapsed.microseconds/1000)+"ms")


if __name__ == '__main__':
    pytest.main(['-s','test_request_demo.py'])

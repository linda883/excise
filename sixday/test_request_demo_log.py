import requests
import log
import yaml
import pytest
from ddt import ddt, file_data, unpack


@ddt
class TestMsg:

    Log = log.LOG

    @file_data('data.yaml')
    @unpack
    def test_post_get(self, **data):
        print(data)
        url = data.get('url')
        method = data.get('method')
        test_data = data.get('payload')
        print(test_data, url, method)
        post_msg = requests.request(method=method, url=url, data=test_data)
        self.Log.info("code:"+str(post_msg.status_code))
        self.Log.info(post_msg.text)
        self.Log.info("time:"+str(post_msg.elapsed.microseconds/1000)+"ms")


if __name__ == '__main__':
    pytest.main(['-s','test_request_demo.py'])

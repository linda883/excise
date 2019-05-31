import pytest
from selenium import webdriver
import logging

log = logging.getLogger(__name__)


class TestClass:

    @pytest.fixture(scope="module", autouse=True)
    def inin_driver(self):
        log.info('setup_class()')
        # cls.driver = webdriver.Firefox()
        # cls.driver.get("http://www.baidu.com")
        log.info("成功打开百度")
        yield
        log.info('teardown_class()')

    @pytest.fixture()
    def init_data(self):
        log.info('test_data_setup')
        yield
        log.info('teardown test_data')

    @pytest.fixture(autouse=True)
    def screen_shot(self):
        log.info("screen_shot")

    @pytest.mark.usefixtures
    def test_qqq(self, init_data):
        log.info("xxxxxxxxxxxqqqq")
        assert 4 == 5

    @pytest.mark.slow
    def test_7(self):
        import time
        time.sleep(5)
        log.info('- test_7()')

    @pytest.mark.qq
    def test_4(self):
        log.info('- test_4()')

    def test_5(self):
        log.info('- test_4()')
        assert 4 == 5

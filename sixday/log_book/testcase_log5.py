from logger5 import *
import pytest


class TestClass():

    @pytest.fixture(scope='session', autouse=True)
    def setupClass(self):
        init_logger()

    def test_logger(self):
        user_log.info("my test.")
        user_log.error("error")
        user_log.critical("critical")
        user_log.warning("warning")
        user_log.debug("debug")
        user_log.notice("notice")


if __name__ == "__main__":
    pytest.main()

import pytest


@pytest.fixture()
def login():
    print("\n这是登陆模块")


def test_soso():
    print('\nsearch baobi')


def test_pay(login):
    print("pay this order")

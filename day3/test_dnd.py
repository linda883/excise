from dnd import attack_damage
from unittest import mock
import pytest


@mock.patch("dnd.randint", return_value=5, autospec=True)
def test_attack_damage(mock_randint):
    assert attack_damage(1) == 6
    print(mock_randint.mock_calls)
    mock_randint.assert_called_with(1,8)


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_dnd.py'])

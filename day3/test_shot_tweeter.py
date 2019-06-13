import unittest
from unittest.mock import Mock
import shot_tweeter


class TestTweet(unittest.TestCase):
    def test_example(self):
        mock_twitter = Mock()
        shot_tweeter.tweet(mock_twitter, "message and")
        mock_twitter.mock_calls
        mock_twitter.PostUpdate.assert_called_with("message and")

    def test_example2(self):
        mock_twitter = Mock()
        shot_tweeter.tweet(mock_twitter, "message")
        mock_twitter.mock_calls
        mock_twitter.PostUpdate.assert_called_with("message")


if __name__ == '__main__':
    unittest.main()

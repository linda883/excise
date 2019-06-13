from users import Users
import unittest
from unittest.mock import patch


class TestUsers(unittest.TestCase):
    @patch('users.Users.list_users')
    def test_user_set(self, mock_list_users):
        mock_list_users.return_value.status_code = 200
        mock_list_users.return_value.json.return_value = {"data":[
            {"id":4,
             "email":"eve.holt@reqres.in",
             "first_name":"Eve1",
             "last_name":"Holt",
             "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/marcoramires/128.jpg"
             }]}
        u = Users()
        resp = u.list_users()
        assert resp.status_code == 200
        self.assertEqual(resp.json()['data'][0]['first_name'],'Eve1')


if __name__ == '__main__':
    unittest.main()
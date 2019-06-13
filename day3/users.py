import requests

BASE_URL = "http://reqres.in"


class Users:
    def list_users(self):
        resp = requests.get(BASE_URL+'/api/v2/users?page=2')
        return resp


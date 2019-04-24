# -*- coding:utf-8 -*-
import json


data = {'name': 'linda', 'age': 18}
data_tuple = (1, 2, 3, 4, 5)
data_list = [1, 2, 3, 4]
# 将Python对象编码成json字符串
json_data = json.dumps(data)
print(json_data)

print(json.loads(json_data))


my_dict = {"login": {"username": "888888", "password": "8888888"}, "loginout": {"un6": "777777", "pd": "333333"}}

with open("login1.json", "w") as f:
    json.dump(my_dict, f)


with open('login.json', 'r+') as f1:
    data = json.load(f1)
    print(data['login'])
    print(data['loginout'])

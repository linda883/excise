# -*- coding:utf-8 -*-
import json
#
#
# data = {'name': 'linda', 'age': 18}
# data_tuple = (1, 2, 3, 4, 5)
# data_list = [1, 2, 3, 4]
# # 将Python对象编码dict成json字符串str
# print(type(data))
# json_data = json.dumps(data)
# print(json_data)
# # 将json字符串str转成python对象dict
# print(json.loads(json_data))


my_dict = {"login": {"username": "888888", "password": "8888888"}, "loginout": {"un6": "777777", "pd": "333333"}}
print(type(my_dict))
# 把my_dict的dict的通过dump方法转成json的str写入文件
with open("login2.json", "w") as f:
    json.dump(my_dict, f)

# 把json文件读出来，转成dict通过key读value,如果是json格式 是读不出来的
# with open('login.json', 'r+') as f1:
#     data = json.load(f1)
#     print(data['login'])
#     print(data['loginout'])

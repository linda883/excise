import json
# try:
#     f = open('test_data.txt', 'r')
#     text = f.read()
#     print(text)
#     f.close()
# except FileNotFoundError:
#     print("file is not found")

with open('test_data.txt', 'r') as f:
        mytxt = f.read()
        print(mytxt)
        # txt_dict = json.loads(mytxt)
        # print(txt_dict)
        # print(type(txt_dict))
        print(mytxt['loginout'])
        # json_str = json.dumps(txt_dict)
        # print(json_str)


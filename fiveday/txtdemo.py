# help(open)

# 编写一个txt文件
# 读
f = open("myfile.txt")
text = f.read()
print(text)
f.close()

with open("myfile.txt") as f:
    myfile = f.read()
    print(myfile)

my_list = ["login","username","888888", "password", "8888888"]
my_dict_str = '{"login": {"username": "888888", "password": "8888888"}, "loginout": {"un6": "777777", "pd": "333333"}}'

my_dict = {"login": {"username": "888888", "password": "8888888"}, "loginout": {"un6": "777777", "pd": "333333"}}

with open("my_dict.txt", "w+") as f:
    f.write(my_dict_str)



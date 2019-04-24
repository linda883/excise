print("请求输入数字：")
a = input()          # 从控制台输入内容放到变量a
flag = int(a)       # 输入的内容默认是字符串的
if flag == 1:
    print("喝奶")
elif flag == 2:
    print("吃饭")
elif flag == 3:
    print("吃大餐")
else:
    print("不吃")

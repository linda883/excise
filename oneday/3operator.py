a = True
b = False

if (a and b):
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

a = 10
b = 20
my_list = [1, 2, 3, 4, 5]




if (a in my_list):
    print("1 - 变量 a 在给定的列表中 list 中")
else:
    print("1 - 变量 a 不在给定的列表中 list 中")

if (b not in my_list):
    print("2 - 变量 b 不在给定的列表中 list 中")
else:
    print("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if (a in my_list):
    print("3 - 变量 a 在给定的列表中 list 中")
else:
    print("3 - 变量 a 不在给定的列表中 list 中")




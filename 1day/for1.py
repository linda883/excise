# 查找列表中某个值是否在列表中
a = 'f'
b = ['a', 'b', 'c', 'd']
for my in b:
    if a == my:
        print("找到！")
        break
else:
    print("没找到！")

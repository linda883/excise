# 跳过某个字母不输出
for letter in 'Python':     # 第一个实例
    if letter == 'h':
        continue
    print('当前字母 :', letter)


a = 'f'
b = ['a', 'b', 'c', 'd']
for my in b:
    if a == my:
        print("找到！")
        break
else:
    print("没找到！")

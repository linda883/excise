a = ["num1", "num2", "num3"]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)  # 返回一个对象
print(list(zipped))  # list() 转换为列表

# print(list(zip(a, c)))  # 元素个数与最短的列表一致
# a1, a2 = zip(*zip(a, b))  # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
# print(list(a1))
# print(list(a2))
# #
# # a, b = b, a
#
# for a, b in zip(a, b):
#     print(a, b)

# 10以内的偶数输出

# lists = [11, 12, 2.3, 9.7]
# print(list(reversed(lists)))
# print(reversed(lists))
# print(list(sorted(lists)))
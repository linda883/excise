# 快速添加数据的小技巧
ls = [1, 2, 3, 4]
list1 = [i for i in ls if i > 2]
print(list1)
list2 = [i*2 for i in ls if i > 2]
tuple1 = (2, 4, 6)
dict1 = {x: x**2 for x in tuple1}
print(dict1)
dict2 = {x: 'item'+str(x**2) for x in tuple1}
print(dict2)
# 将某些不符合字符在要添加的字符串中去掉，
set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)

# 去重的两种方法，一种利用set不可重复，一种是dict不可重复
a = [1, 2, 4, 2, 4, 5, 6, 5, 7, 8, 9, 0]
a1 = list(set(a))
print(a1)
b = {}
b = b.fromkeys(a)
print(b)
c = list(b.keys())
print(c)
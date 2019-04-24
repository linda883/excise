my_str = "I love Python"
my_list = ["python", "java", "lanuage", "age"]
my_list2 = [24, 12, 2.3, 9.7]
my_tuple = ("python", 33, "java", 8.8)
my_dict = {"name": "linda", "age": 88}
my_list1 = ['a', 'a', 1, 1, 2, 3]
my_set = {1, 2, 3}

a = 10
print(type(a))
# 强制转换从int到str
a1 = str(a)
print(type(a1))
# str 转 int
print(type(int(a1)))
# list与tuple元组转换
print(tuple(my_list))
print(list(my_tuple))
# 列表转成set变成不重复的
print(set(my_list1))
# 字典类型转成set只有key值
print(set(my_dict))
# 字典转成列表，key,value可以单转
print(list(my_dict.values()))
print(list(my_dict))
my_tuple1 = ('one', 1), ('two', 2), ('three', 3)
my_list_tuple = [('one', 1), ('two', 2), ('three', 3)]
# print(my_tuple1)
print(type(my_list_tuple))
print(dict(my_list_tuple))



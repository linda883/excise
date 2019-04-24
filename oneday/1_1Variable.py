# 等号是赋值不是等于，是把右边的放到左边的一个名字叫my_int的变量位置中
# 变量以字母开头，大小写敏感，不能是关键字，字母数字下划线
my_int = 10
# 输出类型
print(type(my_int))
my_str = "I'mlove Python"
# 查看有哪些方法
print(dir(my_str))
# 元组，固定长度不能变
my_tuple = ("python", 33, 8.3, 8.8)

# 列表，可变长度，有序
my_list = ["python", 12, 2.3, 9.7, 12]

# 字典，无顺序，按key-value方式存储
my_dict = {'name': 'linda', 'age': 88}

'''
集合，元素无重复
一行可多个语句，使用;分开就行
三个单引或双引表示多行注释
'''
my_set = {1, 2, 3}; print(dir(my_set))
my_bool = True
print(my_bool)


a = b = c = 1
print(a, b, c)
a, b, c = 1, 2, "linda"
print(a,b,c)

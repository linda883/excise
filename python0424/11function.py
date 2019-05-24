# def hello_func(greeting, name='linda'):
#     return '{} {} 你好.'.format(greeting, name)
#
#
# print(hello_func('hi'))
# print(hello_func('hi', 'tom'))
#
#
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# courses = ['python', 'java']
# info = {'name': 'linda', 'age': 18}
# student_info(*courses, **info)


# def foo(x, *args, a=4, **kwargs):  #使用默认参数时，注意默认参数的位置要在args之后kwargs之前
#     print(x)
#     print(a)
#     print(args)
#     print(kwargs)
#
#
# foo(1, (5, 6, 7, 8), {"y": 2, "z": 3})
# foo(1, *(5, 6, 7, 8), **{"y": 2, "z": 3}, a=6)   #调用函数，不改默认参数

# 匿名函数
add = lambda x, y: x+y
add1 = lambda *args: sum(args)
print(add1(1, 56, 35))
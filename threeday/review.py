
# def hello_func(greeting, name=None, age=18):
#     return "{},{} {}function".format(greeting, name, age)
#
#
# a=hello_func("hi", age=88, name="jame")
# print(a)


# def hello_func(*args):
#     print(type(args))
#     return "这是参数值 ："+str(args)
#
#
# a=hello_func(['python', 'java'])
# print(a)

# def hello_func(*args, **kwargs):
#     print(type(args))
#     print(type(kwargs))
#
#     return args, kwargs
#
#
# courses = {'name':'python','name2':'java'}
# courses1= ['python','java']
# a=hello_func(1, (5, 6, 7), **courses)
# print(a)

add = lambda x, y : x+y
print(add(5,6))
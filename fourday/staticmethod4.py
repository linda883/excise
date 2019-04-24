class Foo(object):
    """类三种方法语法形式"""
    name = 'yadang'

    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))

    @staticmethod
    def static_method():
        print("是静态方法")

    @classmethod
    def class_method(cls):
        print("是类方法")


foo = Foo()
foo.instance_method()
# 当实例没有自己的name时，调用的是类的属性name的值
print(foo.name)
# 给实例赋值后，再调用的实例属性就是新的了。
foo.name = 'linda'
print(foo.name)
foo.static_method()
foo.class_method()
print('---------下面是直接通过类调用-------')
print(Foo.name)
Foo.static_method()
Foo.class_method()
# Foo.instance_method()


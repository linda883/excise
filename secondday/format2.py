print('Hi, %s, you have $%d.' % ('linda', 100000000))

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))  # 保留小数点后1位
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置

print("网站名：{name}, 地址 {url}".format(name="测试开发", url="testing-studio.com"))
# 通过字典设置参数
site = {"name": "测试开发", "url": "testing-studio.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['测试开发', 'testing-studio.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的
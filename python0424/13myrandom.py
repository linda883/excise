# import time
# import os
#
# # 生成的测试报告的名字是根据当前时间和文件名全名的。
# report_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
# print(report_time+"_"+os.path.basename(__file__))


import random
import string

# 将序列中的某个随机取出来做为测试数据。序列可以是列表，字符串等
courses = ['python', 'java', 'selenium', 'appium']
random_course = random.choice(courses)
print(random_course)

# 大写小写字母和数字随机拼接为测试数据
rad_str = ''.join(random.choice(string.ascii_uppercase\
                               + string.ascii_lowercase + string.digits)\
                  for _ in range(8))
print(rad_str+"@163.com")


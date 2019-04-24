import time

time.sleep(5)
#
# reporttime=time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
# print(reporttime)
# '''
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
'''
# import random
# import string
# courses = ['python','java','selenium','appium']
#
# random_course = random.choice(courses)
# print(random_course)
#
#
# radstr = ''.join(random.choice(string.ascii_uppercase \
#                                +string.ascii_lowercase+ string.digits) for _ in range(8))
# print(radstr+"@163.com")
# ------
'''

import requests

res = requests.get('http://testing-studio.com')
print(res.text)
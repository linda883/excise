# 关于字符串的操作
str = 'python 蟒蛇'

print(dir(str))
'''
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',\
 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', \
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', \
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''
print(str.count("l"))
print(str.find("o"))
print(str.capitalize())
print(str.encode("gb2312"))
print(str.find("n"))
print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符（-1代表最后一个，左闭右开）
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第四个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串
print(len(str))
print(str.startswith("python"))
b = "20"
print(b.isdecimal())
print(str.upper())
print(str.title())
str0 = 'python 蟒蛇'
print((str0.replace(str0[0:6], "java".upper())))
print(str*4)

s1 = "-"
s2 = ""
seq = ("l", "i", "n", "d", "a") # 字符串序列
print(s1.join(seq))
print(s2.join(seq))

str4 = "编号 标题 测试数据 测试结果"
(no, title, test_data, test_result) = str4.split(" ")
print(test_data)

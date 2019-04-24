#
# # 1、将一些字符替换成另一些的字符并大写。把python换成java变成大写
# str = 'python 蟒蛇'
# print(str.replace(str[0:6], "java".upper()))
#
# # 2、快速复制一个字符串
# str =" 1"
# str1= str*10
# print(str1)
#
# # 3、将字符串的序列通过某个字符（或空）连在一起
# s1=":"
# seq = ("l", "i", "n", "d", "a")
# print(s1.join(seq))
#
#
# # 4、将字符串按某个字符分隔开输出
# str3 = "我说:我今天很高兴！"
# str4 = "编号 标题 测试数据 测试结果"
#
# (no,title,testdata,testresult)=str4.split(" ")
# print(testdata)

# print('Hi, %s, you have $%d.' % ('linda', 100000000))
print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125))
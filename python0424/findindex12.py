#


print("imported my_module")

test = 'Test String'


def find_index(to_search, target):
    # 给出在哪个字符串中找,要查询的target二个参数
    # 在序列进行循环for，找很多次，每一个你都比较一下是不相等，如果相等就是我们要找的。否则返回-1
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

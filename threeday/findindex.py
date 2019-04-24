#


print("imported my_module")

test = 'Test String'


def find_index(to_search,target):
    # 给出一个要找的字符串，还有一个目标序列（一大堆）,要查询的target
    # 在序列进行循环for，找很多次，每一个你都比较一下是不相等，如果相等就是我们要找的。if
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

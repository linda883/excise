'''
这是我写的第一个封装的代码要在pypi上发布试试，主要功能利用递归读取列表数据
'''


# the_list是要输出的列表
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
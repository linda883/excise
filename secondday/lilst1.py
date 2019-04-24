# 列表：以中括号开头结尾，数据通过逗号隔开，使用引号
book = ["python", "java", "appium", "selenium"]
print(book)
print(book[1])          # 输出book列表中第2个
print(len(book))        # 列表的长度
book.append("today history")
book.append("tomorrow history")         # 在后面追回数据
book.pop(2)                             # 删除第3个数据
book.insert(2, "furture history")       # 将数据插入第3位置
book.extend(book)                       # 在列表后面追加另一个列表
book.remove("tomorrow history")         # 在列表中找到并删除一个特定项
book.pop()                              # 删除最后一个
print(book)
print(book.copy()*4 + book)          # 拷贝4遍+一遍
print(book.copy().clear())           # 删除全部
book = ['Google', 'testerhome', 'testing-studio', 'Baidu']
book.reverse()
print("列表反转后: ", book)
book.sort()
print("列表排序后: ", book)
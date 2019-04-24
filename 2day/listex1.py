book = ["python", "java", "man"]
# 1 输出book列表中第2个
# print(book[1])
# 2 列表的长度len
# print(len(book))
# 3 在后面追加数据append
# book.append("data stucture")
# book.append("data stucture")
print(book)
# 4 删除第3个数据pop
# book.pop(1)
# print(book)
# 5 将数据插入第2位置insert
book.insert(1,"data")
print(book)
# 6在列表后面追加另一个列表expand
book.extend(book)
print(book)
# 7 在列表中找到并删除一个特定项remove
book.remove("linda")
print(book)
# # 8 将列表顺序反转  reverse()
# book.reverse()
# print(book)
# # 9 将列表排序 sort()
# book.sort()
# print(book)
# print(book.count("man"))
# book.clear()

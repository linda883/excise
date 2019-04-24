set1 = {1, 2, 3}
set2 = set1
set3 = set("hello")
print(set3)
set3.add(1)
print(set1, set3)
print(set1)
# set3.clear()
print(set3)
de = set3.pop()
print(de)
set3.remove("l")
a = set1 & set3
print(a)
a = set1 | set3
print(a)

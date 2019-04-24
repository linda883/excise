ages = {
    'linda': 18,
    'leimeng': 51,
    'yujian': 31
}
print(ages.get("linda", 88))
ages["dalu"] = 33
ages["yujian"] = 55
print(ages)
del ages['leimeng']
print(ages)
# key in dict
D = {'username': 'linda', 'age': 12, 'salary': 10000000}
print("循环出来key,再通过key可能输入值")
for key in D:
    print(key, '=>', D[key])

print("只循环出值")
for value in D.values():
    print(value)

print("同时循环出key与value，断言返回key的值与...通常用在接口测试中json的响应断言")
for key, value in D.items():
    print(key, ':', value)
    assert D[key] == value

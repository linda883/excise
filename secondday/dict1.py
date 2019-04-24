ages ={
    'linda': 18,
    'leimeng': 51,
    'yujian': 31
}
print(ages.get("linda",88))
ages["dalu"] =33
ages["yujian"]=55
print(ages)
del ages['leimeng']
print(ages)
# key in dict
D = {'username': 'linda', 'age': 12, 'salary': 10000000}
for key in D:
    print(key, '=>', D[key])

for value in D.values():
    print(value)
for key, value in D.items():
    print(key,':',value)
    assert D[key] == value

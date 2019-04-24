ages ={
    'linda': 18,
    'leimeng': 51,
    'yujian': 31
}
# 通过key来访问对应value，如果没有这个key返回默认值。
# print(ages.get("linda", 88))
#
# # 插入一个新的key和value,更新已有的key的值。=
# ages["maine"]=20
# ages["linda"]=28
# print(ages)
# # 删除一个key:  del   clear
# del ages["leimeng"]
# print(ages)
# 遍历字典中的key,value,所有。

for key in ages:
    print(key,"->",ages[key])

for value in ages.values():
    print(value)

for key,value in ages.items():
    print(key,":",value)
    assert ages[key] == value



ls = [1,2,3,4]
list1=[i for i in ls if i>2]
print(list1)

tuple1=(2,4,6)
dict1= {x: x**2 for x in tuple1}
print(dict1)


dict2= {x: 'item'+str(x**2) for x in tuple1}
print(dict2)
#
set1 = {x for x in 'hello world' if x not in 'low level'}
print(set1)
#
seq = ('Google', 'Runoob', 'Taobao','Taobao')
dict = dict.fromkeys(seq)

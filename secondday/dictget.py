ages ={
    'linda': 18,
    'leimeng': 51,
    'yujian': 31
}
# 通常
if 'linda' in ages:
    age = ages['linda']
else:
    age = 'Unknown'

print(age)

# 技巧

age = ages.get('linda', 'Unknown')
print(age)



func_dict={
    'cond_a':11,
    'cond_b':22,
}

print(func_dict.get('cond_a',18))
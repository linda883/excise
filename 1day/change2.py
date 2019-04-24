from collections import Counter
my_str = "I love Python"
my_list = ["python", "java", "lanuage", "age"]
my_list2 = [24, 12, 2.3, 9.7]
my_tuple = ("python", 33, "java", 8.8)
my_dict = {"name": "linda", "age": 88}
my_list1 = ['a','a',1,1,2,3,'a']
my_set = {1, 2, 3}

# 列表中每个元素出现几次

my_couter = Counter(my_list1)
print(my_couter.most_common())



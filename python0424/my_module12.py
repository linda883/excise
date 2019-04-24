import sys
# sys.path.append('/Users/lindafang/Downloads')
from findindex12 import find_index, test

print(sys.path)
courses = ['python', 'java', 'black test', 'selenium']
# 在相同的路径下

index = find_index(courses, 'java')
print(index)
print(test)

def file1():
    f = open('log.txt', 'r')
    for i in f:
        print(i)
    return i


file1()



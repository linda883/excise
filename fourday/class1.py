class SportMan(object):

    def __init__(self, name, score):
        self.__name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


man1 = SportMan("linda", 88)
man2 = SportMan("sevenriby", 33)
print(man1)
print(SportMan)
man1.print_score()
print(man1.score, man1.get_grade())

# print( man2.score, man2.get_grade())



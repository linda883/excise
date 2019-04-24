class SportManList(list):

    def __init__(self, a_name,a_livetime=None, a_times=[]):

        self.a_name = a_name
        self.live = a_livetime
        self.extend(a_times)

    def top3(self):
        # 返回不重复的记录前5--set
        return(sorted(set([t for t in self]))[0:3])


jame = SportManList('jame')
jame.live = '2018-01-01'
jame.append('2.34')
jame.append('3.45')
print(jame.a_name)
print(jame.live)
print(jame.top3())
jame.extend(['5.23', '6.45', '2.56', '2.34'])
print(jame.top3())











class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        print(a,b,c)
        pass

    def closer(self,something):
        something.close()


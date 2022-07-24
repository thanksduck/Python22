a,b=100,200
class MyClass():
    a,b=10,20
    def add(self,a,b):
        print(a+b)
        print(globals()['a']+globals()['b'])
        print(self.a+self.b)
    def mul(self,a,b):
        print(a * b)
        print(globals()['a'] + globals()['b'])
        print(self.a * self.b)
c = MyClass()
c.add(3, 3)
c.mul(4, 4)

# output:
"""
6
300
30
16
300
200"""
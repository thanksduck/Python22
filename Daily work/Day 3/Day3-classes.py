class myclass:
    x=5
ob=myclass()
print(ob.x)

class person:
    def __init__(self,nam,ag):
          #init-> fxn which is called automatically everytime class is used to create new objects, it acts as a constructor (initialize values to data members of class when object is created)
          # default constructor-> which don't accept any arguments; parametarised constructor-> has parameters
        self.name=nam
        self.age=ag
    def myfxn(myins):  
          #self,myins etc are my instances i can name them anything i want and they are used to refer my variables of the class.it is always1 parameter of fxn
        print('name is '+myins.name)

p1=person('sukhman',20)
print('name =',p1.name)
print('age =',p1.age)

p2=person('simran',18)
print('name =',p2.name)
print('age =',p2.age)

p3=person('sarbjeet',21)
print('name =',p3.name)
print('age =',p3.age)

del p1.age   #deletes the property of age for object p1
# print('age =',p1.age)  #->printing this will give an error as it has been deleted

p1.myfxn()
p2.myfxn()
p3.myfxn()

class testclass():
  def __init__(self,y):
    self.x=y
  def testfxn(self):
    self.name=input('enter your name :')
    self.age=int(input('enter your age :'))
t1=testclass(10)
print(t1.x)
print(t1.testfxn())

class employee():
  def __init__(self):
    print('employee created')
  def __del__(self):
    print('destructor called')
      #destructors are called when object gets destroyed. it is called when all referances to the object have been deleted, ie when an object is garbage collected.destructor called after prog ended or after all referances to object are deleted. 
obj=employee()
del obj
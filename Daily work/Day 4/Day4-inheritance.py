class person(): #base class
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.__age=20  #this is the private member of class
    def display(self):
        print(self.name,self.id)
p1=person('sukhman',101)
p1.display()

class employee(person): #derived from class person,this is eg of single inheritance
    def prnt(self):
        print('employee class called')
e1=employee('simran',102)  
e1.prnt()
e1.display()

''' NOTE
types of inheritance:-
single->one class drived from one base class
multiple-> derived class is derived from 2 or more base classes
mulitlevel-> class 3 derived from class 2 which was derived from class 1
hierarichal-> more than one derived class from same base class
hybrid->combine more than one form of inheritance
'''
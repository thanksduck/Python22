# Example 1
from abc import ABC, abstractmethod
class Animal(ABC):
  @abstractmethod
  def eat1(self):
   pass
@abstractmethod
def eat2(self):
   pass
class Tiger(Animal):
 	def eat1(self):
 		print("Tiger implementation ...")
class lion(Tiger):
 	def eat2(self):
 		print("lion implementation ...")
t = lion()
t.eat1()
t.eat2()

"""1)Output
Tiger implementation ...
lion implementation ..."""S
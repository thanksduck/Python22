class TooYoungException(Exception):
   def __init__(self,age):
         self.age=age
class TooOldException(Exception):
   def __init__(self,age):
         self.age=age
try:
   age=int(input("Enter Age:"))
   if age<18:
     raise TooYoungException("Plz wait some time ")
   elif age>65:
     raise TooOldException("Your age too old")
   else:
     print("we will find one girl soon")
except TooYoungException as e:
     print("Plz wait some time ")
except TooOldException as e:
     print("Your age too old ")

"""5) Output
Enter Age: 16
Plz wait some time 

Enter Age:20
we will find one girl soon

Enter Age:66
Your age too old"""
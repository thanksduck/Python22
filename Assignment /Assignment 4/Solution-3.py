def status(age):
     if age < 0:
         raise ValueError("Only positive integers are allowed")
     if age>22:
         print("eligible for mrg")
     else:
         print("not eligible for mrg try after some time")
try:
     num = int(input("Enter your age: "))
     status(num)
except ValueError:
     print("Only positive integers are allowed you ......")
finally:
     print("finally block....")

"""Output
Enter your age: -9
Only positive integers are allowed you ......
finally block....

Enter your age: 21
not eligible for mrg try after some time
finally block....

Enter your age: 34
eligible for mrg
finally block....
"""
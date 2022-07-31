class Vehicle:
     def __del__(self):
         print("Vehicle object destroyed")
         print(10/0)
v = Vehicle()
del v

"""9)output
Vehicle object destroyed
    print(10/0)
ZeroDivisionError: division by zero"""
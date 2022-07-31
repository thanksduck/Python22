class Customer:
    def __init__(self,name,bal=0.0):
         self.name=name
         self.bal=bal
 
    def deposit(self,amount):
         self.bal=self.bal+amount
    def withdraw(self,amount):
         if amount>self.bal:
             raise RuntimeError("withdraw amount is more than balance")
         else:
             self.bal=self.bal-amount
 
    def remaining(self):
        return self.bal
c = Customer("Komal",10000)
damt = int(input("enter amount to deposit : "))
c.deposit(damt)
amt = int(input("enter amount to withdraw : "))
c.withdraw(amt)
print(c.remaining())

"""10)Output
enter amount to deposit : 90000
enter amount to withdraw : 30000
70000"""

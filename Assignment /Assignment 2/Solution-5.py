#calculator
choice = input("Enter operator to use:")
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))
if choice == '+':
   ans=A+B
elif choice == '-':
   ans=A+B
elif choice == '*':
   ans=A+B
elif choice == '/':
   ans=A+B
else:
   print("Invalid input")

print("the answer is",ans)
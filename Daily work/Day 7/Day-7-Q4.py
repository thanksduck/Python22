#4) 1200 to 3000 numbers are divisible by 4 and 8 but not divisible by 6 
#first method
lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for i in range(lower, upper+1):
   if((i%4==0) & (i%8==0) & (i%6!=0)):
              print (i)

#second method
for i in range(1200, 3000): 
	if i%4==0 and i%8==0 and i%6!=0: 
            print(i)
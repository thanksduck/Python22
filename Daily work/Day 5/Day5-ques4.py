''' take numbers between 1200 and 3000 and print the no if it is divisible by 4 and 8 but not by 6'''
for i in range(1200,3000):
    if i%4==0 and i%8==0 and i%6!=0:
        print(i)
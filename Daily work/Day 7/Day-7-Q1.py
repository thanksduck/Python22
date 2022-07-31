#1) Given l1 = ['m' , 'n'] and n=3 show that output ['m1', 'm2', 'm3', 'n1', 'n2', 'n3']
l1 = ['m','n']
n=3
new_list = ['{}{}'.format(x,y) for y in range(1, n+1) for x in l1]
print(new_list)
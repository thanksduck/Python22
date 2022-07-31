#3) Remove the duplicate number [1,2,3,0,1,1,4,5,2,3]
list1 = ["1","2","3","0","1","1","4","5","2","3"]
list1 = list(dict.fromkeys(list1))
print(list1)
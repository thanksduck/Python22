''' remove the duplicate items from the list
[1,2,3,0,1,1,4,5,2,3]
'''
l1=[1,2,3,0,1,1,4,5,2,3]
l1=list(dict.fromkeys(l1)) 
print(l1)
     #changing the list into dictionary and formimg elements of list as keys removes all the duplicate elements as dictionary cnt have duplicate items, then converting the dictionary back into the list to print the desired result.
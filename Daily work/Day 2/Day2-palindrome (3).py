string1= input('enter the string: ')
n=len(string1)
i=0
if string1[i]==string1[n-1]:
    i+=1
    n-=1
    print('the string is palindrome')
else:
    print('the string is NOT a palindrome')
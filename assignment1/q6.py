print()
print("############ answer 6 ##############")
str="string"
if(str[-3:]!='ing'):
    print('expected result:' ,str + 'ing')
else:
    print("expected result:", str[:-3] + 'ly')
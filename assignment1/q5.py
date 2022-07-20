print()
print("############ answer 5 ##############")
def string_mix(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    print(new_a +' '+ new_b)
print(string_mix('abc','xyz'))
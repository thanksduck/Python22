a ="fast"
if len(a) < 3:
    x = a
elif a[-3:] == "ing":
    x = a + "ly"
else:
    x = a + "ing"
print (x)
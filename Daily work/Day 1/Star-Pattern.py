# print given pattern
#  ****
#  ****
#  ****
#  ****
print('rectangular star pattern')
for x in range(4):
 for y in range(4):
  print('*',end='')
 print()

#  print given pattern
# *
# **
# ***
# ****
print('right triangle star pattern')
for i in range(0, 4):
 for j in range(0, i+1):
  print("* ",end="")
 print("\r")
#Average of list elements
numbers = [6, 5, 3, 8, 4, 2, 5, 6, 11]
sum = 0
for i in numbers:
    sum = sum + i
    avg = sum/len(numbers)

print("The average is", avg)
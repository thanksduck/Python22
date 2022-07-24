string="This is a sample Python program, Welcome to World Of Python Programming!"
word="Python"
list=[]
wordCount=0
list=string.split(" ")
for i in range(0,len(list)):
      if(word==list[i]):
            wordCount=wordCount+1
print("Number of occurrences found in the string:")
print(wordCount)
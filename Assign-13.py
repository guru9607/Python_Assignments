#Program to find the length of a list using recursion

list =["Guru","Tushar","Bot",2]

#Finding length of provided list

listLength=len(list)
print("The length of a list is:",listLength)

#Finding length of provided list in additive way

count=0
element=0
for element in list:
    count=count+1

print("The length of a list is: ", count)

#Finding length of provided list in recursive way

# 1)
def list_length(list):
   if not list:
      return 0
   return 1 + list_length(list[1::1]) 
print("The list is :")
print(list)
print("The length of the string is : ")
print(list_length(list))

# 2)
len = 0
def length(list):
   global len
   if list:
      len = len + 1
      length(list[1:])
   return len

len = length(list)
print("The length of a list is", len)

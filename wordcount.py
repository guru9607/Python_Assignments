str1= "Hello NCER Hello CSE Hello mech"
word="Hello"
List=[]
wordcount=0
List = str1.split(" ")
for i in range(0,len(List)):
    if(word == List[i]):
        wordcount=wordcount+1

print("No. of occurances found in string is: ")
print(wordcount)

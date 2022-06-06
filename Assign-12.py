#Program to read a file and capitalise the first letter.

newFile = open("Assign-12.txt", "x")
newFile.close()

newFile = open("Assign-12.txt", "w")
newFile.write("hello world!")
newFile.close()

fileName = input("Enter your file name bro: ")
 
with open(fileName, 'r') as file:
    for line in file:
        capLine=line.title()
        print(capLine)

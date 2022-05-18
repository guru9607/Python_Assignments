import operator
str="Study for main exam"
substring2="exam"

print("Does",substring2,"exists","in",str,"?")

if operator.contains(str, substring2):
    print("Yes")
else:
    print("False")

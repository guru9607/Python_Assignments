str="Study for main exam"
substring2="exam"

print("Does",substring2,"exists","in",str,"?")

V=str.find(substring2)
if V>=0:
    print("Yes")
else:
    print("No")

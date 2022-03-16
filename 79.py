str=input("enter the string")
u=0
l=0
for i in str:
    if (i.islower()):
        l=l+1
    else:
        u=u+1
print("count",l,"count",u)

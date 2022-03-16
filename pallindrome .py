m=int(input("enter the number"))
rev=0
n=m
while m>0:
    b=m%10
    m=m//10
    rev=rev*10+b
if n==rev:
    print("pallindrome number")
else:
    print("not pallindrome number")
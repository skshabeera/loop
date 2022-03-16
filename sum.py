n=int(input("enter the number"))
sum=0
while n>0:
    a=n%10
    n=n//10
    sum=sum+a
print(sum)
n=int(input("enter the number"))
mul=1
while n>0:
    a=n%10
    n=n//10
    mul=mul*a
print(mul)
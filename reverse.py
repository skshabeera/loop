# n=int(input("enter the number"))
# rev=0
# while n>0:
#     a=n%10
#     b=a
#     rev=rev+b
#     n=n//10
# print(rev)
# n=int(input("enter the number"))
# str1=" "
# while n>0:
#     c=n%10
#     a=c
#     b=str(a)
#     n=n//10
#     str1+=b
# print(str1)
n=int(input("enter the number"))
rev=0
while n>0:
    b=n%10
    n=n//10
    rev=rev*10+b
print(rev)

    
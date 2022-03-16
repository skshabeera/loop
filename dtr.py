# n=int(input("enter the number"))
# a=n
# s=0
# while n>0:
#     f=1
#     i=1
#     r=n%10
#     while i<=r:
#         f=f*i
#         i=i+1
#     s=s+f
#     n=n//10
# if s==a:
#     print("s")
# else:
#     print("n")
n=1
while n<=1000:
    a=n
    s=0
    while a>0:
        f=1
        i=1
        r=a%10
        while i<=r:
            f=f*i
            i=i+1
        s=s+f
        a=a//10
    if s==n:
        print(s)
    n=n+1


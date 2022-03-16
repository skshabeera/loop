sentence="My position is 14st and my friend come on 1th"
a="0"
sum=0
for i in sentence:
    if (i.isdigit()):
        a+=i
    else:
        sum+=int(a)
        a="0"
print(sum)

    
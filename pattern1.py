i=0
m=9
j=1
while i<4:
    if i==0 or i==3:
        for i in range(0,4):
            print(j+i,end="  ")
            j=j+4
        print()
        i=i+1
    else:
        for i in range(0,4):
            print(j+m,end=" ")
            m=m+4
    print()
    i=i+1
            
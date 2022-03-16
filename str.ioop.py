n=int(input("enter the number"))
i=0
str=str(n)
str1=" "
while i<len(str):
    if str[i]=="0":
        str1+="zero"
    elif str[i]=="1":
        str1+="one"
    elif str[i]=="2":
        str1+="two"
    elif str[i]=="3":
        str1+="three"
    elif str[i]=="4":
        str1+="four"
    elif str[i]=="5":
        str1+="five"
    elif str[i]=="6":
        str1+="six"
    elif str[i]=="7":
        str1+="seven"
    elif str[i]=="8":
        str1+="eight"
    elif str[i]=="9":
        str1+="nine"
    i=i+1
    str1+=" "
print(str1)
    
    
    
    
    
    
    
    
    
    
    



def st(str):
    new_str=""
    i=len(str)-1
    while(i>=0):
        new_str=new_str+str[i]
        i=i-1
    return new_str
s=input("Enter a string ")
print("The reversed string is : ",st(s))

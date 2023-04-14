def expo(a,b):
    if(b==0):
        return 1
    else:
        return (a*expo(a,b-1))
x=int(input("Enter the number of x"))
y=int(input("Enter the number of y"))
print("Result is ",expo(x,y))

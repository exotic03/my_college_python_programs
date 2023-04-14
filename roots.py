a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
d=(b**2)-(4*a*c)
r1=(-b+d**0.5)/2*a
r2=(-b-d**0.5)/2*a
if(d>0):    
    print("Different roots")
    print(r1)
    print(r2)
elif(d==0):
    print("Same roots")
    print(r1)
    print(r2)
else:
    print("Imaginary roots")
    print(r1)
    print(r2)


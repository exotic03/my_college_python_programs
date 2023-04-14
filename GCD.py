def gcd(a,b):
    r=a%b
    if(r==0):
        return b
    else:
        return gcd(b,r)
x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
print("The GCD is :",gcd(x,y))

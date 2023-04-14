b=int(input("Enter a binary number : "))
i=0
d=0
r=0
while(b!=0):
    r=b%10
    d=d+r*(2**i)
    b=b//10
    i=i+1
print("Equavalent Decimal number is : ",d)

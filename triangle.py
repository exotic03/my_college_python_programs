a=int(input("Enter the 1st side"))
b=int(input("Enter the 2nd side"))
c=int(input("Enter the 3rd side"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area is : ",area)

n=int(input("Enter the number : "))
temp=n
sum=0
while(n>0):
    r=n%10
    sum=sum+(r**3)
    n=n//10
if(temp==sum):
    print("This is a Armstrong number")
else:
    print("This is not a Armstrong number")

n=int(input("Enter a number : "))
sum=0
for i in range (1,n+1):
    if(i%2==0):
        r=i**2
    else:
        r=0
    sum=sum+r
print("Sum of square of even numbers is ",sum)

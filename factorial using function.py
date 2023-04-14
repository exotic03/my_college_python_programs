def fact(n):
    sum=1
    for i in range(1,n+1):
        sum=sum*i
    return sum
num=int(input("Enter a number: "))
f=fact(num)
print("The factorial of number is : ",f)

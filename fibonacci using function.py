def fibo(n):
    a=0
    b=1
    print("The fibonacci series is :")
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
r=int(input("Enter the range : "))
fibo(r)
        
        

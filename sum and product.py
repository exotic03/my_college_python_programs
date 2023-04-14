n=int(input("enter  number"))
sum=0
pro=1
while(n>0):
    r=n%10
    if(r%2==0):
        sum=sum+r
    else:
        pro=pro*r
    n=n//10
print(sum,pro)

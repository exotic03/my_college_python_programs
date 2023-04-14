def avg(*a):
    sum=0
    for i in a:
        sum=sum+i
    return sum/len(a)
av=avg(5,3,7,8)
print("The average is :",av)

def large(a,b):
    if(a>b):
        return a
    else:
        return b
sum=lambda x,y:x+y
sub=lambda x,y:x-y
print("larger number is ",large(sum(10,8),sub(10,5)))

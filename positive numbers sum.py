def pos(*args):
    t=0
    for i in args:
        if(i>=0):
            t=t+i
    return t
print("Sum of positive number is ",pos(1,-2,3,5,-4))

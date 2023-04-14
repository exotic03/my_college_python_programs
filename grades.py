a=int(input("Enter the number of 1st subject"))
b=int(input("Enter the number of 2nd subject"))
c=int(input("Enter the number of 3rd subject"))
d=int(input("Enter the number of 4th subject"))
e=int(input("Enter the number of 5th subject"))
f=(a+b+c+d+e)/5
if(f>=90):
    print("Outstanding")
elif(f>=80 and f<90):
    print("Excellent")
elif(f>=70 and f<80):
    print("Very good")
elif(f>=60 and f<70):
    print("Good")
elif(f>=50 and f<60):
    print("satisfactory")
else:
    print("failed")

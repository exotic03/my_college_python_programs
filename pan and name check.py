name=input("Enter your name : ")
if(name.isalpha()==False):
    print("Invalid name")
else:
    pan=input("Enter your pan number : ")
    if(pan.isalnum()==False):
        print("Invalid pan number")
    else:
        print("please check ",name,"your pan number is ",pan)

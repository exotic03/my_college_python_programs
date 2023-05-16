list=[]
for i in range(1,11):
    list.append(i)
print("The list is :",list)
for i in list:
    if(i%2==0):
        list.remove(i)
print("The list after remove the even numbers",list)

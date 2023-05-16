length=int(input("Enter a range : "))
list=[]
for i in range(1,length+1):
    list.append(i)
print("The list is :",list)
l=len(list)
for i in range(l//2):
    temp=list[i]
    list[i]=list[l-1-i]
    list[l-1-i]=temp
print("The reversed list is :",list)

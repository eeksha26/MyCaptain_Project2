list=[]
n=(int)(input("Enter number of elements to add in the list:"))
for i in range(0,n):
    new=(int)(input("Enter a number:"))
    list.append(new)
newlist=[]
for i in list:
    if i>0:
        newlist.append(i)
print(newlist)

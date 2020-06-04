n=(int)(input("Enter the number of terms you want to display:"))
a=0
b=1
print("{}\n{}".format(a,b))
i=2
while i<n:
    c=a+b
    print("{}".format(c))
    a=b
    b=c
    i=i+1
print("DONE!")

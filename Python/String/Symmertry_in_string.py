a=input("Enter Name:- ")
mid=(len(a)-1)//2
x=a[0:mid+1]
y=a[mid+1:len(a)]
if x==y:
    print("YES")
else:
    print("NO")
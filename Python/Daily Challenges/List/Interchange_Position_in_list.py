def interchange_position(a,pos1,pos2):
    temp=a[pos1-1]
    a[pos1-1]=a[pos2-1]
    a[pos2-1]=temp
    return a
a=list(map(int,input("Enter elements:- ").split(" ")))
pos1=int(input("Enter Position 1:- "))
pos2=int(input("Enter Position 2:- "))
print(a)
print(interchange_position(a,pos1,pos2))

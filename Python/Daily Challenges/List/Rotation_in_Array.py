a=list(map(int,input("Enter elements in array: ").split(" ")))
r=int(input("Enter number of rotations:-"))
print("Array Before:",a)
n=len(a)
for i in range(0,r):
    temp=a[0]
    for j in range(0,n-1):
        a[j]=a[j+1]
    a[n-1]=temp
print("Array After:",a)
#-------------------------------Approach 2
def rotation(a,r):
    x=[]
    x.append(a[:r]) #x will store first r elements 
    d=[element for element in a if element not in x[0]] #d will store all other elements
    d.extend(x[0])#now add x elements in d 
    return d
a=list(map(int,input("Enter elements in array: ").split(" ")))
r=int(input("Enter number of rotations:-"))
print(rotation(a,r))

def linearsearch(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x=110
res=linearsearch(arr,x)
if res!=-1:
    print("Element is at Position "+str(res+1))
else:
    print("Element is Not Present")

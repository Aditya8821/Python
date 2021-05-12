def BinarySearch(arr,low,high,x):
    if low<=high:
        mid=(low+high)//2
        if x>arr[mid]:
            return BinarySearch(arr,mid+1,high,x)
        elif x<arr[mid]:
            return BinarySearch(arr,low,mid,x)
        else:
            return mid
    else:
        return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
res=BinarySearch(arr,0,len(arr)-1,x)
if res!=-1:
    print("Element is at Position "+str(res+1))
else:
    print("Element is Not Present")
        

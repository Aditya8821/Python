def binarysearch(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if x>arr[mid]:
            low=mid+1
        elif x<arr[mid]:
            high=mid
        else:
            return mid
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 10
res=binarysearch(arr,x)
if res!=-1:
    print("Element is at Position "+str(res+1))
else:
    print("Element is not present in Array")
    

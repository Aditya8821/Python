def BubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1): #Here n-i-1 Bcoz largest element is reached to its pos(top) previous pass
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[64,34,25,12,22,11,90]
BubbleSort(arr)
print("Sorted Array: "+str(arr))
                
                

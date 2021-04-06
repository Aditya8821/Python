a=list(map(int,input("Enter elements in array:- ").split(" ")))
maximum=a[0]
for i in range(1,len(a)):
    if a[i]>maximum:
        maximum=a[i]
print(maximum,"is the maximum element")
#--------------------------------Approach 2
print(max(a),"is the maximum element")

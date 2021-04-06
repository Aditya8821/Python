def is_monotonic(a):
    return(all(a[i]<=a[i+1] for i in range(len(a)-1))or(all(a[i]>=a[i+1] for i in range(len(a)-1))))
a=list(map(int,input("Enter elements:-").split(" ")))
print(is_monotonic(a))

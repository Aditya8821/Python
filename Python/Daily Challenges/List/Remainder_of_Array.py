def remainder(a,n):
    mul=1
    for i in range(0,len(a)):
        mul*=a[i]
    return mul%n
a=list(map(int,input("Enter elements:- ").split(" ")))
n=int(input("Enter divisor value:-"))
print(remainder(a,n))

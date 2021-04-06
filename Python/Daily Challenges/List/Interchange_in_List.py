def interchange(a):
    temp=a[-1]
    a[-1]=a[0]
    a[0]=temp
    return a
a=list(map(int,input("Enter elements:-").split(" ")))
print(a)
print(interchange(a))

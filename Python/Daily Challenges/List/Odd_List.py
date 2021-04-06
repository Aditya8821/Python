def oddlist(a):
    x=[]
    for i in a:
        if i%2!=0:
            x.append(i)
    return x
a=[1,2,3,4,5,6]
print(oddlist(a))

def evenlist(a):
    x=[]
    for i in a:
        if i%2==0:
            x.append(i)
    return x
a=[1,2,7,5,9,42,63]
print(evenlist(a))

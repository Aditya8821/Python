def remove(a):
    for i in a:
        if i%2==0:
            a.remove(i)
    return a
a=[1,2,3,4,5,6,7,8,9]
print(remove(a))
#-----------------------Approach2
a=[1,2,3,4,5,6,7,8,9]
b=[k for k in a if k%2!=0]
print(b)

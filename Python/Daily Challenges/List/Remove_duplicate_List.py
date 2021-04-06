def remove_duplicate(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    return b
a=[2,4,3,2,5,6,3,5,4,8,1,3]
print(remove_duplicate(a))

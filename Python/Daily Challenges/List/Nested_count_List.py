l=[3,4]
b=[]
for i in range(len(l)):
    l[i]=[i+1 for k in range(l[i])]
print(l)

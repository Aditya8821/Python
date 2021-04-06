list=[["Gfg", "good"], ["is", "for"]]
res=[]
f=[]
for i in range(len(list[0])):
    for j in range(len(list)):
        res.append(list[j][i])
    s=("".join(res))
    f.append(s)
print(res)

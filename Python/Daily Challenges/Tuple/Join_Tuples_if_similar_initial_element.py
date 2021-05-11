test_list = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
res=[]
for i in test_list:
    if res and res[-1][0]==i[0]:
        res[-1].extend(i[1:])
    else:
        res.append([ele for ele in i])
res=list(map(tuple,res))
print(res)

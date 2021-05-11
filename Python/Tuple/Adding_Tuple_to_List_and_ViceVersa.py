lis=[5,6,7]
tup=(9,8)
lis+=tup
print("Adding Tuple in List: "+str(lis))
lis=[5,6,7]
res=tuple(list(tup)+lis)
print("Adding List in Tuple: "+str(res))

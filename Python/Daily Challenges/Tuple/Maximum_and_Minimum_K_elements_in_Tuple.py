test_tup = (5, 20, 3, 7, 6, 8)
k=2
l=sorted(list(test_tup))
result=list(l[0:k]+l[-k:])
print("Output:- "+str(result))

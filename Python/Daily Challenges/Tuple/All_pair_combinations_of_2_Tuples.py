tuple1 = (4, 5)
tuple2 = (7, 8)
res=[(a,b) for a in tuple1 for b in tuple2]
res=res+[(a,b) for a in tuple2 for b in tuple1]
print("All combinations: "+str(res))

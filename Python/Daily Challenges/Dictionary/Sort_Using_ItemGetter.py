from operator import itemgetter
lis = [{ "name" : "Nandini", "age" : 20}, { "name" : "Manjeet", "age" : 20 },{ "name" : "Nikhil" , "age" : 19 }]
res=sorted(lis,key=itemgetter('age'))
print("Sorted by age:"+str(res))
res=sorted(lis,key=itemgetter('age','name'))
print("Sorted by name and age:"+str(res))
res=sorted(lis,key=itemgetter('age'),reverse=True)
print("Ascending order of age:"+str(res))
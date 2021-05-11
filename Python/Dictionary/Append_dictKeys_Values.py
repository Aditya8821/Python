from itertools import chain
test_dict = {"Gfg" : 1, "is" :  3, "Best" : 2}
res=list(chain(test_dict.keys(),test_dict.values()))
print("List of Keys and Values:"+str(res))
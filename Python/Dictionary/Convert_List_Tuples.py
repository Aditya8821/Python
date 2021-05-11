def convert(tup,dict):
    for a,b in tup:
        dict[a]=[b]
    return dict
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dict={}
print(convert(tups,dict))

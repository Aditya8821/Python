tup = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))
keys = ['key', 'value', 'id']
res=[{key: val for key,val in zip(keys,sub)} for sub in tup]
print(res)

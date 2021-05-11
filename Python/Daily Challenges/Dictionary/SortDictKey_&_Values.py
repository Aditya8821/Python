inp={'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}
res={key :sorted(inp[key]) for key in sorted(inp)}
print("Sorted Dict: "+str(res))
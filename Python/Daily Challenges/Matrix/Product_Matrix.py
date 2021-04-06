list = [[1, 4, 5],[7, 3],[4],[46, 7, 3]]
mul=1
for i in range(len(list)):
    for j in range(len(list[i])):
        mul*=list[i][j]
print(mul)
    

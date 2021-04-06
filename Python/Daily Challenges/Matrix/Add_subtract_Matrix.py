a = [[1,2],[3,4]]
b = [[4,5],[6,7]]
add=[[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
sub=[[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
print(add)
print(sub)

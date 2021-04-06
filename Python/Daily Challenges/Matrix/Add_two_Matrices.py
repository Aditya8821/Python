x=[[1,2,3],[4 ,5,6],[7 ,8,9]]
y=[[9,8,7],[6,5,4],[3,2,1]]
b=[[x[i][j]+y[i][j] for j in range(len(x[0]))] for i in range(len(x))]
print(b)

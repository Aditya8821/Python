lis = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k=1
res=[ele for ele in lis if len(ele)!=k]
print(res)

def break_chunks(a,n):
      return [a[ele:ele+n] for ele in range(0,len(a),n)]
a=[1,2,3,4,5,6,7,8,9]
n=4
print(break_chunks(a,n))

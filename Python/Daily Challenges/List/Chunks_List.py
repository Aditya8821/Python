def break_chunks(a,n):
    b=[]
    for i in range(0,n):
        x=yield a[i:i+n]
      
a=[1,2,3,4,5,6,7,8,9]
n=4
print(break_chunks(a,n))

def cumulative_sum(a):
    sum=0
    b=[]
    for i in range(0,len(a)):
        sum+=a[i]
        b.append(sum)
    return b
a=[10,20,30,40,50]
print(cumulative_sum(a))

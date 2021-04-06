def least_frequent(str):
    d={}
    for i in str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    result=min(d,key=d.get)
    return result
str = "GeeksforGeeks"
print("Least Frequent Character Used In The Given String:",least_frequent(str))
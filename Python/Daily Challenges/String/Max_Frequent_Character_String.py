def max_frequent(str):
    d={}
    for i in str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    result=max(d,key=d.get)
    return result
str = "GeeksforGeeks"
print("Maximum Frequent Character Used In The Given String:",max_frequent(str))
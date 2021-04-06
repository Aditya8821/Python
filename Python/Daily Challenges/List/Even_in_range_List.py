def even_in_range(start,end):
    x=[]
    for i in range(start,end+1):
        if i%2==0:
            x.append(i)
    return x
start=int(input("Enter starting of range:- "))
end=int(input("Enter ending of range:-"))
print(even_in_range(start,end))

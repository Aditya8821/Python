def count_Occurrence(a,x):
    count=0
    for i in a:
        if i==x:
            count+=1
    return count
a=[2,3,2,5,3,4,5,1]
print(count_Occurrence(a,3))
#---------------------------Approach 2
print(a.count(3))

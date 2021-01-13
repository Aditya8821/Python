import collections
l=[1,2,1,4,2,5,3,3,2,1]
a=collections.Counter(l)
print(a)
print(a[1])
a[1]=5
x=list(a.elements())
print(x)
y=a.most_common(2)
print(y)
a=collections.Counter([1,1,2,2,2])
b=collections.Counter([1,1,1,2,3])
print(a|b)
print(a&b)

def multiply(a):
    mul=1
    for i in a:
        mul*=i
    return mul
a=[1,2,3,4]
print(multiply(a))
#---------------------Approach2
a.reverse()
print(a)
print(sum(a))
print(min(a))
b=[4,2,6,1,5]
n=int(input("Number of largest elements:-"))
b.sort()
for i in range(1,n+1):
    print(b[-i])
    

        

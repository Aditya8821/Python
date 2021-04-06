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

        

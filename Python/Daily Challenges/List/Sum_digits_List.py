def sum_digits(a):
    b=[]
    for num in a:
        sum=0
        while(num!=0):
            sum+=num%10
            num=num//10
        b.append(sum)
    return b
a=[12,67]
print(sum_digits(a))

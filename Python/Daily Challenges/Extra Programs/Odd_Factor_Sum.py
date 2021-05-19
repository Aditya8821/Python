def oddfactorsum(n):
    sum=0
    for i in range(1,int(n/2+1)):
        if n%i==0 and i%2!=0:
            sum+=i
    print(sum)
n=30
oddfactorsum(n)

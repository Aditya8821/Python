def primefactor(n):
    for i in range(2,n+1):
        if n%i==0:
            isprime=1
            for j in range(2,int(i/2+1)):
                if i%j==0:
                    isprime=0
                    break
            if isprime:
                print(i)
n=315
primefactor(n)
                               
                           

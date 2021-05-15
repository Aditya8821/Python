def staircase(n):
    for i in range(1,n+1):
        if i%2!=0:
            k=n//2-i+1
        else:
            k=n//2-i+2
        for j in range(1,n+1):
            if j==k:
                if i%2!=0:
                    for o in range(1,i+2):
                        print("*",end=" ")
                    print("\n")
                else:
                    for e in range(1,i+1):
                        print("*",end=" ")
                    print("\n")
            else:
                print(" ",end=" ")
                
n=10
staircase(n)
                

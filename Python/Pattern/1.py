x=int(input("Enter number:="))
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=i:
            print("*",end=" ")
    print()

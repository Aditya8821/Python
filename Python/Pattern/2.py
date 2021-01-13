x=int(input("Enter number:="))
x+=1
for i in range(1,x):
    for j in range(1,x):
        if j>=x-i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

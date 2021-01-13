a,b,c=int(input("a=")),int(input("b=")),int(input("c="))
d=b*b-4*a*c
if d>0:
    print("Roots are Real and Different")
elif d==0:
    print("Roots are Real and Same")
elif d<0:
    print("Roots are Complex")
    

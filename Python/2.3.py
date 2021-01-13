"""Wap to check given number is Positive Negative or Zero"""
x=int(input("Enter a number:"))
if x==0:
    print("ZERO")
else:
    r=(lambda x:"POSITIVE" if x>0 else "NEGATIVE")(x)
    print(r)

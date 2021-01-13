"""Wap to check Leap Year"""
"""Year must be divisible by 4 or if it is divisible by 100 then it must be with 400"""
y=int(input("YEAR:-"))
if y%4==0:
    if y%100==0:
        if y%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    ("Not aLeap Year")

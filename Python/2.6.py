"""Wap to take month value in numeric format and display no. of days in numerical format"""
y=int(input("Year-"))
x=int(input("Month-"))
if x==1 or x==3 or x==5 or x==7 or x==9 or x==11:
    print("31 DAYS")
elif x==2:
    print("28 DAYS")
elif x==2 and y%4==0 or y%100==0 and y%400==0:
    print("29 DAYS")
else:
    print("30 DAYS")

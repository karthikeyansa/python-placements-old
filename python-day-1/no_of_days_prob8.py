from datetime import date
d1=int(input("enter a day"))
m1=int(input("enter a month"))
y1=int(input("enter a year"))
d2=int(input("enter an another day"))
m2=int(input("enter an another month"))
y2=int(input("enter an another year"))
date1=date(y1,m1,d1)
date2=date(y2,m2,d2)
result = date1 - date2
a=int(result.days)
if a<0:
    a=-(a)
print("Differences between two dates are: %d"%a)

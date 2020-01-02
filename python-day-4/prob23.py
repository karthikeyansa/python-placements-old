l1=list(input('enter the integers:').split())
l2=[]
for i in l1:
    if i.isdigit():
        l2.append(i)
print(l2)

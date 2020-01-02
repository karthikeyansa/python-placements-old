l1=list(map(int,input('enter the keys: ').split()))
l2=list(map(int,input('enter the values: ').split()))
l3=[]
d={}
for i in l2:
    l3.append(i*i)
for j in range(len(l1)):
    d.update({l1[j]:l3[j]})
print(d)

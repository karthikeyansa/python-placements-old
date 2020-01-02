l1=list(map(int,input('enter the keys: ').split(',')))
l2=list(map(int,input('enter the values:').split(',')))
d={}
for i in range(len(l1)):
    d.update({l1[i]:l2[i]})
print(d)

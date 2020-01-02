l1=list(map(int,input('enter key separated by comma').split(',')))
l2=list(map(int,input('enter value separated by comma').split(',')))
d={}
for i in range(len(l1)):
    d.update({l1[i]:l2[i]})
print(d)

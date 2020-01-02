n=int(input('enter a value:'))
l1=[x for x in range(1,n+1)]
l2=[x for x in range(1,n+1)]
l3=[]
d={}
for i in l2:
    l3.append(i*i)
    
for j in range(len(l1)):
    d.update({l1[j]:l3[j]})
    
print(d)

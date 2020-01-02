l1=set([1,3,6,78,35,55])
l2=set([12,24,35,24,88,120,155])
m=[]
for i in list(l1):
    if i in list(l2):
        m.append(i)
print(*m,sep=',')

l1=set([12,24,35,24,88,120,155])
m=[]
for i in l1:
    if i != 24:
        m.append(i)
m.sort()
print(*m,sep=',')

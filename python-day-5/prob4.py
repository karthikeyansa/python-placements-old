n=list(map(int,input('enter the list of numbers separated by comma: ').split(',')))
c=set(n)
m=[]
for i in c:
    m.append(i)
m.sort()
print(*m,sep=',')
    


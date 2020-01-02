n=str(input('enter the string: '))
m=[]
for i in n:
    if not i.isdigit():
        m.append(i)
print(*m,sep='')

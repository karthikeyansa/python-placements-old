l1=[12,24,35,70,88,120,155]
c=0
for i in l1:
   
   if c == 0:
       l1.remove(i)
   elif c == 4:
       l1.remove(i)
   elif c == 5:
       l1.remove(i)
   c+=1
print(l1)

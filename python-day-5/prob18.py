n=int(input('enter number of items:'))
l1=[int(n) for n in input('enter the number').split()]
c=0
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        print('this item==>',i)
        

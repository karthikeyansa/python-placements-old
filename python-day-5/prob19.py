n=int(input('enter the limit:'))
l1=[int(n) for n in input('enter the number:').split()]
print(l1)
l1.sort()
l1.reverse()
print(*l1,sep='')

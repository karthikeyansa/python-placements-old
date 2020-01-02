l=int(input('enter low value: '))
h=int(input('enter the value: '))
for i in range(l,h+1):
    if i>0:
        for j in(2,i):
            if j % i == 0:
                break
            else:
                print(i)

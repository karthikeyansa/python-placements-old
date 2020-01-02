namt=0
while True:
    op,val=input("enter deposit/withdrawl and value separated by space: ").split()
    c=int(val)
    if op == input():
        break
    elif op == 'd' or op == 'D':
        namt += c
    elif op == 'w' or op == 'W':
        namt -= c
print("bank account net amount",namt)

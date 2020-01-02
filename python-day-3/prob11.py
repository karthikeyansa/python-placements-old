def prime(n):
    if n>0:
        for i in range(2,n):
            if i % 2 == 0:
                print('not prime')
                break
n=int(input('enter a number: '))
prime(n)

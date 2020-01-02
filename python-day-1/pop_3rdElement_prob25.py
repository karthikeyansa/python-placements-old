def remove(n):
    i=0
    pos=2
    len_n=len(n)
    while len_n != 0:
        i=(pos+i)%(len_n)
        print(n.pop(i))
        len_n-=1
n=list(map(int,input("ENTER THE LIST NUMBERS SEPARATED BY SPACE: ").split()))
print(remove(n))
        

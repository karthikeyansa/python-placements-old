#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
n=list(map(int,input("enter the list of numbers separated by comma: ").split(',')))
m=[]
c=0
for i in n:
    if i % 2 != 0:
        c=i*i
        m.append(c)
print(*m,sep=' ')
#question output mistake

from itertools import permutations 
l1=list(map(int,input('enter the integers separated by comma: ').split(',')))
p = permutations(l1) 
for i in list(p): 
    print (i) 

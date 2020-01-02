l1=list(input('enter the keys separate by comma: ').split(','))
l2=list(input('enter the values separate by comma: ').split(','))
d={}
for i in range(len(l1)):
    d.update({l1[i]:l2[i]})
print(d)

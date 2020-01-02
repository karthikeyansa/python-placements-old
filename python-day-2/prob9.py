#9)Write a Python program to replace last value of tuples in a list.\cb1 \
n=list(map(int,input("Enter the items(int) by comma: ").split(',')))
m=int(input("Enter the item(int) to be replaced at last: "))
n[-1]= m
print(tuple(n))

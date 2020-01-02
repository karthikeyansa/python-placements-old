#6)Write a Python program to remove an item from a tuple.\
n=tuple(map(int,input("Enter the set of numbers separated by space: ").split()))
m=int(input("ENTER THE ITEM TO REMOVE: "))
t=list(n)
t.remove(m)
print(tuple(t))

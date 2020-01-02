#4)Write a Python program to find the repeated items of a tuple.\
n=tuple(map(int,input("Enter the set of numbers separated by space: ").split()))
m=[]
for i in n:
    if i not in m:
        m.append(i)
    else:
        print(i,"repeated items")

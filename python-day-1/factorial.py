def fact(x):
    if x == 1:
        return 1
    else:
        return(x * fact(x-1))
n1=int(input("enter the number:"))
print(fact(n1))


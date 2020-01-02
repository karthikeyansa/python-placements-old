n1=int(input("enter the 1st number "))
n2=int(input("enter the 2nd number "))
n3=int(input("enter the 3rd number "))
if n1 > n2 and n1 > n3:
    print("this is number %d is greater"%n1)
elif n2 > n3:
    print("this is number %d is greater"%n2)
else:
    print("this is number %d is greater"%n3)
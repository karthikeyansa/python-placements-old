#Write a Python program to convert a tuple to a string.
n=tuple(map(str,input("Enter the set of numbers separated by space: ").split()))
print(str(n))
print(type(str(n)))

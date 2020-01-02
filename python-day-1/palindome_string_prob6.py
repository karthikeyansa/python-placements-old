n=str(input("enter the string:"))
if n[:] == n[::-1]:
    print("The given string %s is palindrome"%n)
else:
    print("The given string %s is not a palindrome"%n)

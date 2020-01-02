def alphanum(s):
    if s.isalnum():
        return True
    else:
        return False
def alpha(s):
    if s.isalpha():
        return True
    else:
        return False
def lower(s):
    if s.islower():
        return True
    else:
        return False
def upper(s):
    if s.isupper():
        return True
    else:
        return False
    
s=str(input('enter a string: '))
print(alphanum(s))
print(alpha(s))
print(lower(s))
print(upper(s))

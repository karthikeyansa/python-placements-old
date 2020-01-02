s = str(input('enter the string:'))

num = sum(c.isdigit() for c in s)
word   = sum(c.isalpha() for c in s)
sp  = sum(c.isspace() for c in s)
rem  = len(s) - num - word - sp
print('numbers',num)
print('words',word)
print('space',sp)
print('spl',rem)

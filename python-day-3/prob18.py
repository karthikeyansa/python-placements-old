try:
    a=5/0
    b=int(input())
except(ZeroDivisionError,ValueError):
    print('ZeroDivisionError,ValueError')

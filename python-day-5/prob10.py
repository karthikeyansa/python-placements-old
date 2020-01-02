def check(l1):
    for i in l1:
        assert(i % 2 == 0),'even numbers'
        print(i ,'is','even')
    return l1
l1=[2,4,6,8]
print(check(l1))

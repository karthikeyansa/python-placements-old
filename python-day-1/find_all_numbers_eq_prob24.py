n=list(map(int,input("ENTER THE LIST OF NUMBERS SEPARATED BY SPACE: ").split()))
if (len(set(n))==len(n)):
    print("ALL ELEMENTS ARE UNIQUE")
else:
    print("SOME ELEMENTS ARE SAME")

n=list(map(int,input("enter the list of numbers and space to separate them: ").split()))
count=0
for i in n:
    if i == 4:
        count+=1
print("The number of 4's present in the list are: ",count)

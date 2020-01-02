n=[[1,2,3],[2,3,4],[2,3,4]]
m=[[2,3,4],[2,3,4],[2,3,4]]
res=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(n)):
    for j in range(len(n[0])):
        res[i][j]=n[i][j]+m[i][j]
for k in res:
    print(k)

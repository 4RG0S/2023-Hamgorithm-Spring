x=int(input())
for k in range(x):
    y,z=map(int, input().split())
    o=1 
    u=1
    for l in range(1,y+1):
        o=o*l
    
    for t in range(1,y+1):
        u=u*(z-t+1)
    print("%d"%(u/o))
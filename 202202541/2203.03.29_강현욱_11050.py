x, y=map(int,input().split())
z=1
t=1
for k in range(1,y+1):
    z=z*k
for i in range(0,y):
    t=t*(x-i)
print("%d"%(t/z))
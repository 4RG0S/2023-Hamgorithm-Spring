y=int(input())
x=[[0]*2 for p in range(y)]
for z in range(y):
    x[z][0],x[z][1]=map(int,input().split())
key=[1]*y

for gh in range(y):
    for hj in range(y):
        if gh==hj:
            continue
        elif((x[gh][0]<x[hj][0])and(x[gh][1]<x[hj][1])):
            key[gh]+=1
for ty in range(y):
    print(key[ty])
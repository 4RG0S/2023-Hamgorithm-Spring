import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def find(x):
    if(x==parent[x]):
        return x
    parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    parent[a]=b
nod, count= map(int, input().split())
parent=[0]*(nod+1)
for i in range(1,nod+1):
    parent[i]=i
for j in range(count):
    q,w,e=map(int,input().split())
    if(q==0):
        if(w==e):
            continue
        union(w,e)
    elif(q==1):
        if(find(w)==find(e)):
            print("YES")
        else:
            print("NO")


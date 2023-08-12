import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
par = [-1 for i in range(n+1)]
# union - find start
def union(a,b):
    a,b = find(a), find(b)
    if a == b:
        return
    par[b] = a
    return

def find(x):
    if par[x]<0:
        return x
    par[x] = find(par[x])
    return par[x]
for index in range (1,n+1):
    info = list(map(int,sys.stdin.readline().split()))
    # oper = 0 disconnected
    # oper = 1 connected
    for i in range (len(info)):
        # if info is 1 -> connect the node
        if info[i] == 1:
            union(index, i+1)
plan = list(map(int,sys.stdin.readline().split()))
# check roots what i planned
# if root is different, it cannot be connected -> print "NO" 
root = find(plan[0])
flag = "YES"
for i in plan:
    if root != find(i):
        flag = "NO"
        break
print(flag)
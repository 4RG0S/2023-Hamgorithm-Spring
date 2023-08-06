import sys
n , m = map (int, sys.stdin.readline().split())
par = [-1 for i in range (n+1)]
def union(a,b): # 두 집합을 연결
    a,b = find(a),find(b) 
    if a == b:  # 루트 부모가 같다면 같은 집합 => 연결 관계
        return
    par[b] = a # 부모 노드를 통일하여 하나의 집합으로
    return
def find(x):
    if par[x] < 0:
        return x
    par[x] = find(par[x])
    return par[x]

for _ in range (m):
    
    oper , a,b = map (int, sys.stdin.readline().split())
    # oper = 0 이면 union
    # oper = 1 이면 find
    if (oper == 0):
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

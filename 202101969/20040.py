import sys

jum_num, count = map(int, sys.stdin.readline().split())
parent = [i for i in range(jum_num)]
def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]
def Union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        # 부모가 같은경우
        return
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
an = True
for i in range(count):
    a,b = map(int, sys.stdin.readline().split())
    # 부모가 같은 애를 합치면 사이클 생성
    if find(a) == find(b):
        print(i+1)
        an = False
        break # 사이클
    else: # 사이클이 생성되지 않울 땨 union
        Union(a,b)
if an:
    print(0)
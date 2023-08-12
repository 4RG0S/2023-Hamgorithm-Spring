import sys
sys.setrecursionlimit(1000000)
n, m = map(int,sys.stdin.readline().split())

set = [0] * (n + 1)
for i in range(n + 1) :
    set[i] = i
#union-find 알고리즘
def find(a) :
    if a == set[a] :
        return a
    tmp = find(set[a])
    set[a] = tmp
    return set[a]
def union(a , b) :
    a = find(a)
    b = find(b)
    if a == b:
        return
    if a < b:
        set[b] = a
    else : 
        set[a] = b

for i in range(m) :
    x , a , b = map(int,sys.stdin.readline().split())
    if x == 0 : #x가 0이면
        union(a , b) #a와 b가 포함되어있는 집합을 합침
    elif x == 1: #x가 1이면 확인하는 연산 진행
        if find(a) == find(b) :
            print('YES')
        else :
            print('NO')

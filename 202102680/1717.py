import sys
n, m = map(int,input().split())
sys.setrecursionlimit(100000) # 재귀 깊이 제한 늘리기
node = [i for i in range(n+1)]

def find(x): # node[x] != x 의 의미는 다른 어딘 가에 종속되어있다는 것 => 중속된 것을 재귀로 찾아냄
    if node[x] != x:
        node[x] = find(node[x])
    return node[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b: # 작은 거 기준으로 종속
        node[b] = a
    else:
        node[a] = b

for _ in range(m):
    num, a, b = map(int,input().split())

    if a == b and not num:
        continue
    if num: # 두 원소가 같은 집합에 포함 되어 있는 지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else: # num 이 0인 경우 => 합집합 연산
        union(a,b)

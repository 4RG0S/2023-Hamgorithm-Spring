import sys
sys.setrecursionlimit(10**5)

def union(a, b) :
    a = find(a)
    b = find(b)
    if a == b :
        next
    elif a < b :
        arr[b] = a
    else :
        arr[a] = b   

# 루트 노트를 찾는 함수를 재귀적으로 구현        
def find(n) : 
    if arr[n] == n :
        return n
    temp = find(arr[n])
    arr[n] = temp # 루트 노드를 찾아 부모 테이블 갱신
    return arr[n]
    
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [i for i in range(n+1)] 

for i in range(m) :
    cal, a, b = map(int, input().split())
    if cal == 0 :
        union(a, b)
    elif cal == 1 :
        if find(a) == find(b) :
            print("YES")
        else :
            print("NO")
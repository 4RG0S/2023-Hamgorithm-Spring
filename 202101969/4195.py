import sys
def find(x):
    # 부모찾기
    if x == parent[x]:
        return x
    else:
        parent[x] = (find(parent[x]))
        return parent[x]
def Union(x, y):
    #합치기
    x = find(x)
    y = find(y)
    if x == y:
        print(num[x])
        return
    parent[y] = x # 뒤에꺼의 부모를 앞의 꺼로 고치고
    num[x] += num[y] # 개수를 업데이트. 이때 부모의 값을 올림
    print(num[x]) # 올린 값 print


number = int(sys.stdin.readline())
for _ in range(number):
    n = int(sys.stdin.readline())
    parent={}
    num = {}
    for i in range(n):
        a,b = sys.stdin.readline().split()
        # 일단 없으면 생성
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] =1
        # 합치기
        Union(a,b)
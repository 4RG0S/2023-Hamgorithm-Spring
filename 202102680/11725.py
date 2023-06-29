n = int(input())
node = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)


visited = [0] * (n+1)

def dfs(p):
    for a in node[p]:   # node[i] 안에 j가 저장돼있다면 i와 j 가 연결되어있다고 가정
        if visited[a] == 0:     # j를 방문을 하지 않았다면
            visited[a] = p  # 부모 노드인 i를 visited에 저장
            dfs(a)


dfs(1)      # 트리의 루트부터 시작
for i in range(2, n+1):
    print(visited[i])
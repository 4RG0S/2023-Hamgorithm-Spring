from collections import deque

n = int(input())
node = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)


visited = [False] * (n+1)
ans = [0]*(n+1)

def bfs(node, v, visited):
    que = deque([v])    #큐 생성
    visited[v] = True   #방문한 노드 true로 바꿔주기
    while que:  #큐 있을 때
        x = que.popleft()   #맨 처음에 들어온 거 pop
        for i in node[x]:   #노드 안 싹 탐색
            if not visited[i]:  #방문 안했던거면
                ans[i] = x      #부모노드 저장
                que.append(i)   #큐에 넣어줌(탐색하라고
                visited[i] = True   #이미 방문했다고 설정


bfs(node,1,visited) # 트리의 루트부터 시작

for i in range(2, n+1):
    print(ans[i])
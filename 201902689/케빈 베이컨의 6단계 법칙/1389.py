from collections import deque
import sys
input = sys.stdin.readline

user, relation = map(int, input().split(' '))

relations = [[] for _ in range(user + 1)]

for _ in range(relation):
    a, b = map(int, input().split(' '))
    relations[a].append(b)
    relations[b].append(a)

totalLength = [0 for _ in range( user + 1)]
totalLength[0] = 5000

for i in range(1, user+1):

    visited = [False for _ in range(user + 1)]
    distance = [0 for _ in range(user + 1)]
    queue = deque()
    queue.append(i)
    while queue:
        now = queue.popleft()
        if not visited[now]:
            relations[now].sort()
            for node in relations[now]:
                if distance[node] == 0:
                    distance[node] = distance[now] + 1
                else:
                    # 현재 노드 + 1이 다음 노드의 최단거리보다 짧으면 갱신해준다
                    if distance[now] + 1 < distance[node]:
                        distance[node] = distance[now] + 1
            for num in relations[now]:
                queue.append(num)
            visited[now] = True
    distance[i] = 0
    totalLength[i] = sum(distance)
    
print(totalLength.index(min(totalLength)))

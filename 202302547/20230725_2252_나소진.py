import sys
from collections import deque
  
input = sys.stdin.readline
n, m  = map(int,input().split()) # 학생 번호(노드의 개수), 비교 회수(간선의 개수)
indegree = [0] * (n+1) # 진입차수를 저장할 배열
graph = [[] for _ in range(n+1)] # 노드 간의 정보를 저장할 배열

for _ in range(m) : # 진입차수 연산
    a, b = map(int,input().split())
    graph[a].append(b) # A에서 B로 이동
    indegree[b] += 1
    
result = []
q = deque()

for i in range(1, n+1) : # 초기 시작점을 큐에 저장
    if indegree[i] == 0 :
        q.append(i)
        
while q :
    key = q.pop()
    result.append(key)
    for i in graph[key] : # 연결된 노드의 진입차수를 감소시키고 0인지 확인
        indegree[i] -= 1
        if indegree[i] == 0 :
            q.append(i)

for i in result :
    print(i, end=' ')    

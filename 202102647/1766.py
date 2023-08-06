import sys
import heapq
n,m = map(int,sys.stdin.readline().split())
arr = [0]*(n+1)
graph = [[] for _ in range (n+1)] 
result = []
queue = []
for _ in range (m):
    a,b = map (int,sys.stdin.readline().split())
    arr[b] += 1 # a->b b의 차수를 1 늘림
    graph[a].append(b)
# 같은 순위일 땐 숫자가 작은 게 먼저 나와야함. 우선순위큐 사용
for i in range (1,n+1): # 선수문제가 없는 문제는 큐에 우선적으로 넣음
    if arr[i] == 0:
        heapq.heappush(queue, i)

for _ in range (n):
    t = heapq.heappop(queue)
    result.append(t) # 맨앞에 있는 원소를 result에 넣음
    print(t,graph[t])
    for i in graph[t]: # 맨앞 원소의 graph에 들어있는 원소를 얻어냄
        arr[i] -= 1 # 해당 원소의 차수를 줄임 (그래프 연결을 끊음)
        if arr[i] == 0: # 만약 연결된 원소가 아예 없다면 queue에 넣음
            heapq.heappush(queue,i)

for i in result:
    print(i,end=" ")
import queue
n, m = map(int, input().split())
count = [0] * (n + 1)
edge = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    count[b] += 1
    edge[a].append(b)

pq = queue.PriorityQueue()
for i in range(1, n+1):
    if count[i] == 0:
        pq.put(i)
# 자신을 가리키는 노드가 없는 경우 우선순위 큐에 넣는다

while not pq.empty():
    cur = pq.get()
    print(cur, end=' ')
    for next in edge[cur]:
        count[next] -= 1
        if count[next] == 0:
            pq.put(next)
# 우선순위 큐를 통해 자신을 가리키는 노드가 없는 노드 중 숫자가 작은 경우를 가져옴
# count = 0인 next 노드를 pq에 넣어준다
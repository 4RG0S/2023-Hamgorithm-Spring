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

while not pq.empty():
    cur = pq.get()
    print(cur, end=' ')
    for next in edge[cur]:
        count[next] -= 1
        if count[next] == 0:
            pq.put(next)

import queue

n = int(input())
m = int(input())
edge = [[] for _ in range(n+1)]
count = [0 for _ in range(n+1)]
part = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[b].append((a, c))
    count[a] += 1

q = queue.Queue()
for i in range(1, n+1):
    if count[i] == 0:
        q.put(i)

while not q.empty():
    cur = q.get()
    for next, num in edge[cur]:
        if part[cur].count(0) == n + 1:
            part[next][cur] += num
        else:
            for i in range(1, n + 1):
                part[next][i] += part[cur][i] * num
        count[next] -= 1
        if count[next] == 0:
            q.put(next)
for i, x in enumerate(part[n]):
    if x > 0:
        print(i, x)

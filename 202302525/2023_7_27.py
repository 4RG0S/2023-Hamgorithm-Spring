from queue import PriorityQueue

n, m = map(int, input().split())
que = PriorityQueue()
table = [0 for _ in range(n)]  #진입차수
tree = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())

    table[b-1] += 1
    tree[a-1].append(b)

for i in range(n):
        if table[i] == 0:
            que.put(i+1)
            table[i] -= 1
    
for _ in range(n):
    k = que.get()
    print(k)

    for i in tree[k-1]:
        table[i-1] -= 1

        if table[i-1] == 0:
            que.put(i)
            table[i-1] -= 1
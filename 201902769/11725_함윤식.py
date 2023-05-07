import queue

def DFS(start):
    q = queue.Queue()
    q.put(start)
    
    while not q.empty():
        cur = q.get()
        for next in tree[cur]:
            if parent[next]:
                continue
            else:
                parent[next] = cur
                q.put(next)
            
N = int(input())

tree = [[] for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]


for _ in range(N - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

DFS(1)

for i in range(2, N + 1):
    print(parent[i])
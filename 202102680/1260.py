from collections import deque
from sys import stdin
node, edge, start = list(map(int, stdin.readline().split()))

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
        if n in graph:
            temp = list(set(graph[n]) - set(visited))
            temp.sort()
            queue += temp
    return " ".join(str(i) for i in visited)

graph = {}

for i in range(edge):
    edges=stdin.readline().split()
    n1, n2 = [int(j) for j in edges]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph,start))
print(BFS(graph,start))
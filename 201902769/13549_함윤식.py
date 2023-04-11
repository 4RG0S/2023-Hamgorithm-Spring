from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
queue = deque()
queue.append(n)

while queue:
    cur = queue.popleft()
    if cur == k:
        break

    for next in (cur + 1, cur - 1, cur * 2) :

        if 0 <= next <= 100000:
            if visited[next] == 0:
                if next == cur * 2 and next != 0:
                    visited[next] = visited[cur]
                    queue.appendleft(next)
                else:
                    visited[next] = visited[cur] + 1
                    queue.append(next)
                    
print(visited[k])
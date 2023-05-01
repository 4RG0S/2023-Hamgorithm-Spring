from collections import deque
a, b = map(int, input().split(' '))

queue = deque()
for i in range(1, a + 1):
    queue.append(i)
print("<", end="")

while queue:
    for i in range(b - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end="")
    if not queue: break
    print(", ",end="")
print(">")
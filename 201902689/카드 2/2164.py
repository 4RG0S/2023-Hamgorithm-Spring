from collections import deque

num = int(input())
queue = deque()
for i in range(1, num + 1):
    queue.append(i)

while len(queue) != 1:
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
    print(queue)
print(queue.popleft())
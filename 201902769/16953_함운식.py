from collections import deque
queue = deque()

a, b = map(int, input().split())
queue.append((a, 0))
while True:
    if len(queue) == 0:
        print("-1")
        break
    cur, count = queue.pop()
    if cur == b:
        print(count + 1)
        break
    else:
        if cur * 2 <= b:
            queue.append((cur * 2, count+1))
        if cur * 10 + 1 <= b:
            queue.append((cur * 10 + 1, count+1))
from collections import deque

N, K = map(int, input().split(' '))

queue = deque()
for i in range(1, N + 1):
    queue.append(i)
print("<", end='')

while queue:
    for i in range(K):
        tmp = queue.popleft()
        queue.append(tmp)
    tmp = queue.pop()
    print(tmp, end='')
    if queue:
        print(',', end=' ')
print('>')
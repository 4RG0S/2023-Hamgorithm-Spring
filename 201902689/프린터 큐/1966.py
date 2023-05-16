from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    result = 0
    queue = deque()
    arr = list(map(int, input().split(' ')))
    for i in range(len(arr)):
        # (중요도, 인덱스)
        queue.append((arr[i], i))

    count = 0
    while True:
        if queue[0][0] == max(queue, key=lambda x:x[0])[0]:
            count += 1
            # 내가 원하는 순서인지 체크
            if queue[0][1] == M:
                print(count)
                break
            else:
                queue.popleft()
        else:
            queue.append(queue.popleft())


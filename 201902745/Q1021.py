from collections import deque

N, M = map(int,input().split())
data = deque([i for i in range(1,N+1)])
N_list = list(map(int,input().split()))

count = 0
for num in N_list:
    while 1:
        if data[0] == num:
            data.popleft()
            break
        else:
            if data.index(num) <= len(data)//2:
                data.rotate(-1)
                count += 1
            else:
                data.rotate(1)
                count += 1
print(count)

import heapq

N = int(input())

noodles = []
for _ in range(N):
    noodles.append(list(map(int, input().split())))

noodles.sort()

queue = []

for value in noodles:
    heapq.heappush(queue, value[1])
    if value[0] < len(queue):
        heapq.heappop(queue)
        
print(sum(queue))
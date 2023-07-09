import heapq
import collections

people = []
computer = []
visit = {}

arr = []
N = int(input())
m = collections.defaultdict(int)

for _ in range(N):
    fr, to = map(int, input().split())
    arr.append((fr, to))

arr.sort(key=lambda x: x[0])

count = 0
for cur in arr:
    if not people:
        count += 1
        m[count] = 1
        heapq.heappush(people, (cur[1], count))
        continue

    while cur[0] >= people[0][0]:
        heapq.heappush(computer, heapq.heappop(people)[1])
        if not people:
            break 
    
    if not computer:
        count += 1
        m[count] = 0
        heapq.heappush(computer, count)

    m[computer[0]] += 1
    heapq.heappush(people, (cur[1], heapq.heappop(computer)))
    
print(len(m.keys()))
for i in m:
    print(m[i], end=' ')
import heapq
n, k = map(int, input().split())
bag = []
value = []
for _ in range(n):
    m, v = map(int, input().split())
    bag.append([m, v])
for _ in range(k):
    v = int(input())
    value.append(v)
    
bag = sorted(bag)
value = sorted(value)

hq = []
result = 0
for v in value:
    
    while bag and v>=bag[0][0]:
        heapq.heappush(hq, -bag[0][1])
        heapq.heappop(bag)
    if hq:
        result -= heapq.heappop(hq)
        
    
print(result)
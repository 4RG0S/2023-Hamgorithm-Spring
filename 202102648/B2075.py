import sys
import heapq
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
for _ in range(n-1) :
    for i in list(map(int, input().split())):
        if array[0] < i :
            heapq.heappop(array)
            heapq.heappush(array, i)

print(array[0])
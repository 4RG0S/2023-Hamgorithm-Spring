import sys
import heapq #최소힙 사용
input = sys.stdin.readline
 
N = int(input())
pq = []
 
for i in range(N):
    inp = int(input())
 
    if inp==0:
        try:
            print(-heapq.heappop(pq))
        except:
            print(0)
    else:
        heapq.heappush(pq, -inp)
 #push, pop 때 -를 붙이면 최대힙 구현가능
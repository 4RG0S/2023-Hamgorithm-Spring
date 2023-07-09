import sys
import heapq #최소힙 사용
input = sys.stdin.readline 

N = int(input())
pq = []
 
for i in range(N):
    inp = int(input())
 
    if inp==0:
        try:
            print(heapq.heappop(pq)[1])
        except:
            print(0)
    else:
        heapq.heappush(pq, (abs(inp),inp)) #우선순위가 같을 경우 tiebreaker rule 적용
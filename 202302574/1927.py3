import sys
import heapq #최소힙 사용
input = sys.stdin.readline #한줄 단위로 입력받기 때문에, 개행문자가 포함됨
 
N = int(input())
pq = []
 
for i in range(N):
    inp = int(input())
 
    if inp==0:
        try:
            print(heapq.heappop(pq))
        except:
            print(0)
    else:
        heapq.heappush(pq, inp)
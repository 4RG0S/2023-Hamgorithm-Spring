import heapq
# 최소 힙 사용을 위해 heapq import
import sys
input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n) :
    x = int(input())
    if x == 0 : # 입력이 0일 때
        if len(hq) == 0 : # hq가 비어 있으면 0 출력
            print(0)
        else :
            print(heapq.heappop(hq)) # 최소값 출력하고 hq에서 제거
    else : #입력이 0이 아닐 때
        heapq.heappush(hq, x) # 입력을 배열에 추가

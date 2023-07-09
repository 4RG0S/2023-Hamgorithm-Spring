import heapq
import sys

a = sys.stdin.readline
num = int(a())
heap = []

for _ in range(num) : 
    x = int(a())
    # x가 0일 때, heap이 비어있으면 0 출력 / 아니면 최소 원소 반환
    if x == 0 : 
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)*-1) # 원래의 정수를 구현하기 위해 -1 곱하기
    else : 
        heapq.heappush(heap, -x) # 역순으로 저장하기 위해 - 부호를 붙여서 추가
        
    
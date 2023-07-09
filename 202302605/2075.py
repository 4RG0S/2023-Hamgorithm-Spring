import sys, heapq

n = int(input())
heap = []  # heapq 모듈로 일반 리스트를 최소 힙처럼 사용가능

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        heapq.heappush(heap, -1*x)  # 힙에 원소를 추가
                                 # heapq.heappush(추가할 리스트, 추가할 원소)

    else:
        try:
            print(-1*heapq.heappop(heap))  # heapq.heappop(대상 리스트) 
                                        # 가장 작은 원소 값을 리턴 후 삭제
        except:
            print(0)  # 출력할 원소가 없을 경우 0 출력
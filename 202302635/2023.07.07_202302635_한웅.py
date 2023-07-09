import sys
import heapq #힙을 이용해 최소값 쉽게 찾기

N = int(sys.stdin.readline())

h = []

for i in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(h) == 0 :
            print(len(h))  # 배열이 빈 경우 0 출력  
        else :
            print(h[0])    # 이미 정렬이 완료되었으므로 최소값 출력
            heapq.heappop(h) #그 후 최소값 제거
    else :
        heapq.heappush(h,x)

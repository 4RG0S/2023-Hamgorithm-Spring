import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for _ in range(N) :

    i = int(sys.stdin.readline()) # 반복문을 통한 입력은 sys를 활용

    if i == 0 :
        if len(heap) == 0 :
            print("0")
        else :
            print(heap[0]) # 0번째로 최소 원소가 정렬되니, 0번째 원소 출력
            heapq.heappop(heap) # 중복 출력되면 안되니 제거
    else :
        heapq.heappush(heap,i) 
        
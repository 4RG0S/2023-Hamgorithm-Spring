import sys
import heapq  #

N = int(sys.stdin.readline())
h = []

for i in range(N) :
    x = int(sys.stdin.readline())
    if x == 0 :
        if len(h) == 0:
            print(len(h))
        else :
            
            print(-h[0]) #음수로 받았으므로 다시 양수화 시켜서 출력
            heapq.heappop(h)
    else :
        heapq.heappush(h , -x)    #음수로 받아 최댓값 구하기
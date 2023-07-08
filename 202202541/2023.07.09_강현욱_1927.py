import heapq
import sys
input=sys.stdin.readline
heap=[]
x=int(input())
for i in range(x):
    y=int(input())
    heapq.heappush(heap,y)
    #heap 추가
    if(y==0):
        heapq.heappop(heap)
        # 입력값
        if(len(heap)==0):
            print(0)
        else:
            print(heapq.heappop(heap))
        
    

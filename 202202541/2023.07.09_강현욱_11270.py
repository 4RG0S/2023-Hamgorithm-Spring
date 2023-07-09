import heapq
import sys
input=sys.stdin.readline
heap=[]
x=int(input())
for i in range(x):
    y=int(input())

    if(y==0):
        # 입력값 0이면 힙리스트에 추가 안함
        if(len(heap)==0):
            print(0)
        else:
            print(-heapq.heappop(heap))
            #역순 출력 해서 음수 달면 최대값
    else:
        heapq.heappush(heap,-y)
        #역순 저장
    

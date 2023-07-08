import heapq
import sys
input=sys.stdin.readline
x=int(input())
heap=[]
z=[]
for k in range(x):
     z=list(map(int,input().split()))
     for j in z:
          if len(heap)<x:
               heapq.heappush(heap,j)
               #x번쨰 작은수 이므로 x개까지 보관
          else:
               if(heap[0]<j):
                    heapq.heappop(heap)
                    heapq.heappush(heap,j)
                #x번쨰 큰 수 비교해서 추가
print(heapq.heappop(heap))
    #제일작은건 n번쨰수
                    


            
        



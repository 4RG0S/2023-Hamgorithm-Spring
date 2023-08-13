import sys
import heapq
input=sys.stdin.readline
x=int(input())
heap=[]
max_heap=[]
min_heap=[]
for i in range(x):
    y=int(input())
    count_I=0
    count_D=0
    count_min=0
    count_max=0
    for j in range(y):
        com, num=input().split()
        num=int(num)
        if com=='I':
            heapq.heappush(max_heap,-num)
            heapq.heappush(min_heap,num)
            heapq.heappush(heap,num)
            count_I+=1
        elif com=='D':
            if len(heap)!=0:
                count_D+=1
                if count_I>=count_D:
                    if num==1:
                        heapq.heappop(max_heap)
                        heapq.heappop(heap)
                        count_max+=1
                    elif num==-1:
                        heapq.heappop(min_heap)
                        heapq.heappop(heap)
                        count_min+=1
        if len(heap)==1 and (count_min>0 or count_max>0):
            if count_max>=count_min:
                k=-max_heap[0]
            else:
                 k=min_heap[0]
            max_heap.clear()
            min_heap.clear()
            if count_max>=count_min:
                heapq.heappush(max_heap,-k)
                heapq.heappush(min_heap,k)
            else:
                heapq.heappush(min_heap,k)
                heapq.heappush(max_heap,-k)
    if count_I==count_D+1:
        if count_max>=count_min:
            print("%d %d"%(-max_heap[0],-max_heap[0]))
        else:
            print("%d %d"%(min_heap[0],min_heap[0]))
    else:
        if count_I<=count_D:
            print("EMPTY")
        else:
            print("%d %d"%(-max_heap[0],min_heap[0]))
import heapq

N = int(input())
h = []

for i in range(N) :
    a = map(int,input().split())   #5개의 수를 받고
    for j in a :                   #그 수들을 각각 힙에 넣는다
        if len(h) < N :            # 힙의 크기를 N으로 유지시켜 N번째로 큰 수가 제일 작은 수로 남도록 설정
            heapq.heappush(h , j)
        else :
            
            heapq.heappush(h , j)
            heapq.heappop(h)
print(h[0])
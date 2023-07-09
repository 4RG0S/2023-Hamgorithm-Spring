import heapq

hq = []
n = int(input())
# 기본은 최소힙
for i in range(n): # 입력받을 행만큼 반복
    ar = map(int, input().split()) # 입력받은 입력의
    for j in ar: # 원소를 하나씩 빼
        if len(hq) < n: # 만약 더 들어갈 공강이 있다면 넣고
            heapq.heappush(hq, j)
        else: # 없다면
            if hq[0] < j: # 최소값과 비교해본다. 만약 최소값보다 크면
                heapq.heappop(hq) # 기존의 최소값을 버리고
                heapq.heappush(hq, j) # 삽입한다.
print(hq[0])

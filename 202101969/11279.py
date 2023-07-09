import sys, heapq
hq = []
num = int(sys.stdin.readline())
for _ in range(num):
    mum = int(sys.stdin.readline())
    if mum == 0: # 만약 최솟값이고
        if len(hq) == 0: # 현재 hq이 비었다면
            print(0)# 0출력
        else: # 그렇지 않을 경우 최대힙으로 출력
            print((-1)*heapq.heappop(hq))
    else: # 최솟값이 아니라면 최대힙을 유지하면서 push
        heapq.heappush(hq, (-1)*mum)
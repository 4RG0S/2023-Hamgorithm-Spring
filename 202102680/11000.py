import heapq

n = int(input())

que = [list(map(int,input().split())) for _ in range(n)]
que.sort()

check = []
heapq.heappush(check, que[0][1])

for i in range(1,n):
    if que[i][0] < check[0]:    # 다음 수업 시작 시간이 더 빠르면 강의실 하나 더 추가
        heapq.heappush(check, que[i][1])    # check에 다음 수업 끝나는 시간 push
    else:
        # 후의 비교대상 바꿔주기
        heapq.heappop(check)
        heapq.heappush(check, que[i][1])

print(len(check))
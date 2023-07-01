from collections import deque
n, k = map(int, input().split(' '))
visited = [[-1, 0] for _ in range(100001)]

visited[n][0] = 0
'''
    시작점 x에서 이동할 수 있는 방법: x-1, x+1, 2*x
    시작점별로 모든 경우를 bfs로 탐색
    탐색시마다 최소의 경우로 갱신,
    최소 시간, 방법의 리스트
    동일 시간일 경우 방법의 리스트에 추가
'''
def bfs(n):
    queue = deque([n])
    visited[n][0] = 0
    visited[n][1] = 1
    while queue:
        now = queue.popleft()
        for i in [now - 1, now + 1, now * 2]: # 3가지 경우에 대해 탐색해야 하므로 for문으로 가독성 높힘
            if 0 <= i <= 100000:
                if visited[i][0] == -1: # 첫 방문
                    visited[i][0] = visited[now][0] + 1 # 걸린 시간 저장
                    visited[i][1] = visited[now][1] # 방법 수 저장
                    queue.append(i)
                elif visited[i][0] > visited[now][0] + 1: # 이전 방문보다 빠른 시간으로 접근하는 방법
                    visited[i][0] = visited[now][0] + 1
                    visited[i][1] = visited[now][1]
                elif visited[i][0] == visited[now][0] + 1: # 같은 시간이 걸리는 다른 방법인 경우
                    visited[i][1] += visited[now][1] # 방법이 하나 더 있음을 갱신해줌

bfs(n)
print(visited[k][0])
print(visited[k][1])

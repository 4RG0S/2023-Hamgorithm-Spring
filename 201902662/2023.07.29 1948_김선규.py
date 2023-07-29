from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    
    # prev에 각 경로의 진입 차수를 저장
    # load에 각 경로의 자식 노드와 거리를 저장
    prev = [0 for _ in range(n+1)]
    load = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        prev[b] += 1
        load[a].append((b, c))
    
    start, end = map(int, input().split())
    
    # time에 start에서 각 경로까지의 최대 시간을 저장
    # dist에 각 경로까지의 최대 시간을 만드는 직전 경로를 저장
    time = [0 for _ in range(n+1)]
    dist = [[] for _ in range(n+1)]
    que = deque([start])
    
    # 최대 시간을 만드는 경로를 찾으면 time과 dist를 갱신
    # 최대 시간과 같은 시간을 만드는 경로가 있으면 dist에 추가
    # 진입 차수가 0인 경로를 que에 추가
    while que:
        e = que.popleft()
        for d, t in load[e]:
            if time[e] + t > time[d]:
                time[d] = time[e] + t
                dist[d] = [e]
            elif time[e] + t == time[d]:
                dist[d].append(e)
            
            prev[d] -= 1
            if prev[d] == 0:
                que.append(d)
    
    # 그래프 탐색 중 넓이 우선 탐색을 통해 end에서 start까지의 경로를 찾음
    # 찾은 경로를 통해 end에서 start까지의 경로의 개수를 구함
    # 방문한 노드는 다시 방문하지 않도록 visit을 사용
    visit = [True for _ in range(n+1)]
    visit[end] = True
    que = deque([end])
    ans = 0
    
    while que:
        e = que.popleft()
        for i in dist[e]:
            ans += 1
            if visit[i]:
                visit[i] = False
                que.append(i)
    
    print(time[end])
    print(ans)
    
if __name__ == "__main__":
    main()
from collections import deque
import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        # 건물의 개수 n, 건설순서의 개수 k
        n, k = map(int, input().split())
        # 건물 w를 건설완료 하는데 드는 최소 시간
        d = [0] + list(map(int, input().split()))
        # 건물  y를 짓기전 지어야 하는 건물 수
        prev = [0 for _ in range(n+1)]
        # 건물 x를 지어야 짓을 수 있는 건물들
        build = [[] for _ in range(n+1)]
        
        for _ in range(k):
            x, y = map(int, input().split())
            prev[y] += 1
            build[x].append(y)
        
        # 백준이 승리하기 위해 건설해야 할 건물의 번호
        w = int(input())
        # 건설완료하는데 드는 최소 시간을 담는 배열
        time = [0 for _ in range(n+1)]
        # 지어야 하는 건물을 담는 큐
        que = deque()
        
        # 지어야 하는 건물이 없는 건물들을 큐에 담는다.
        # 건설완료하는데 드는 최소 시간은 건물을 짓는데 드는 시간이다.
        for i in range(1, n+1):
            if prev[i] == 0:
                time[i] = d[i]
                que.append(i)
        
        # 지어야 하는 건물을 담은 큐를 순회하며 건물을 짓는데 드는 최소 시간을 구한다.
        while que:
            e = que.popleft()
            for i in build[e]:
                # time[i]에 건물을 짓기 전 지어야 하는 건물들을 짓는데 드는 시간의 최대값을 저장한다.
                time[i] = max(time[i], time[e])
                prev[i] -= 1
                # 건물을 짓기 전 지어야 하는 건물이 없다면
                # 최댓값에 건물을 짓는데 드는 시간을 더하고 건물을 큐에 담는다.
                if prev[i] == 0:
                    time[i] += d[i]
                    que.append(i)
        
        print(time[w])
    
if __name__ == "__main__":
    main()
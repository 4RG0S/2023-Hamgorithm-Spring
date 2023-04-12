from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    maze = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    que = deque([(0, 0, 1)])
    while que:
        v0, v1, val = que.popleft()
        if v0+1 == n and v1+1 == m:
            min_val = val

        if v0+1 < n and maze[v0+1][v1]:
            maze[v0+1][v1] = 0
            que.append((v0+1, v1, val+1))
        if v1+1 < m and maze[v0][v1+1]:
            maze[v0][v1+1] = 0
            que.append((v0, v1+1, val+1))
        if v0 > 0 and maze[v0-1][v1]:
            maze[v0-1][v1] = 0
            que.append((v0-1, v1, val+1))
        if v1 > 0 and maze[v0][v1-1]:
            maze[v0][v1-1] = 0
            que.append((v0, v1-1, val+1))
    print(min_val)
    
if __name__ == '__main__':
    main()
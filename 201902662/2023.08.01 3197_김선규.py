from collections import deque
import sys
input = sys.stdin.readline

def main():
    r, c = map(int, input().split())
    
    # 호수의 상태
    river = [list(input()) for _ in range(r)]
    
    # 2차원 배열의 union find
    parent = [[(i, j) for j in range(c)] for i in range(r)]
    rank = [[1 for _ in range(c)] for _ in range(r)]
    
    def find(n):
        if n == parent[n[0]][n[1]]:
            return n
        parent[n[0]][n[1]] = find(parent[n[0]][n[1]])
        return parent[n[0]][n[1]]

    def union(a, b):
        a = find(a)
        b = find(b)
        
        if rank[a[0]][a[1]] < rank[b[0]][b[1]]:
            a, b = b, a
            
        parent[b[0]][b[1]] = a
        if rank[a[0]][a[1]] == rank[b[0]][b[1]]:
            rank[a[0]][a[1]] += 1
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visit = [[True for _ in range(c)] for _ in range(r)]
    
    # 백조의 위치와 얼음의 위치를 담을 변수
    swan = []
    ice = deque()
    
    # 호수를 모두 순회하며 초기 상태를 지정한다.
    for i in range(r):
        for j in range(c):
            # 얼음이 아니면 bfs를 통해 물 공간을 탐색한다.
            if river[i][j] != 'X' and visit[i][j]:
                visit[i][j] = False
                que = deque([(i, j)])
                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < r and 0 <= ny < c and visit[nx][ny]:
                            visit[nx][ny] = False
                            # 얼음이면 얼음의 위치를 저장한다.
                            if river[nx][ny] == 'X':
                                ice.append((nx, ny))
                            # 물공간이면 union find로 하나의 물공간임을 표시한다.
                            else:
                                union((x, y), (nx, ny))
                                que.append((nx, ny))
            # 백조의 위치를 저장한다.
            if river[i][j] == 'L':
                swan.append((i, j))

    day = 0
    # 같은 물공간이 아닐 동안 반복해서 진행한다.
    while find(swan[0]) != find(swan[1]):
        # 얼음의 위치를 순회한다.
        for _ in range(len(ice)):
            x, y = ice.popleft()
            # 얼음이 녹아 물공간이 되었음을 표시한다.
            river[x][y] = '.'
            # 얼음의 주변을 탐색한다.
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    # 현재 저장되지 않은 얼음이면 저장한다.
                    if river[nx][ny] == 'X' and visit[nx][ny]:
                        visit[nx][ny] = False
                        ice.append((nx, ny))
                    # 물공간이면 union find로 하나의 물공간임을 표시한다.
                    elif river[nx][ny] != 'X':
                        union((x, y), (nx, ny))
        day += 1

    print(day)
    
if __name__ == '__main__':
    main()
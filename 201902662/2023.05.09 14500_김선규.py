from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    tet = [[(0,1),(0,2),(1,1)], [(0,1),(0,2),(-1,1)], [(1,0),(2,0),(1,1)], [(1,0),(2,0),(1,-1)]]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    
    val = 0
    for i in range(n):
        for j in range(m):
            
            st = deque([(i, j, matrix[i][j], [(i,j)])])
            while st:
                x, y, v, c = st.pop()
                if len(c) == 4: 
                    if v > val:
                        val = v
                    continue
                    
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in c:
                        st.append((nx, ny, v + matrix[nx][ny], c+[(nx, ny)]))

            for k in tet:
                v = matrix[i][j]
                for l in k:
                    nx, ny = i + l[0], j + l[1]
                    if 0 <= nx < n and 0 <= ny < m:
                        v += matrix[nx][ny]
                if v > val:
                    val = v
        
    print(val)
    
if __name__ == '__main__':
    main()
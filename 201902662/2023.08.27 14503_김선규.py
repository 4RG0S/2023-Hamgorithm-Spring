import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    cnt = 0
    while True:
        if room[x][y] == 0:
            room[x][y] = 2
            cnt += 1
        
        notClean = True
        for i in range(4):
            nd = (d+3*(i+1))%4
            nx, ny = x + dx[nd], y + dy[nd]
            if room[nx][ny] == 0:
                x, y, d = nx, ny, nd
                notClean = False
                break
        
        if notClean:
            nd = (d+2)%4
            nx, ny = x + dx[nd], y + dy[nd]
            if room[nx][ny] == 1:
                break
            x, y = nx, ny
    print(cnt)
    
if __name__ == "__main__":
    main()
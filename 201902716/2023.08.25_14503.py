import sys

def main():
    N, M = map(int, sys.stdin.readline().split())
    r, c, d = map(int, sys.stdin.readline().split()) # d -> 0: 북, 1: 동, 2: 남, 3: 서
    room = [] # room[r][c] -> 0: 청소 안함, 1: 벽, 2: 청소함
    for _ in range(N):
        room.append(list(map(int, sys.stdin.readline().split())))

    # index -> 0: 북, 1: 동, 2: 남, 3: 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    cnt = 0
    while True:
        cnt_zero = 0 # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸의 개수
        for i in range(4):
            if room[r + dx[i]][c + dy[i]] == 0:
                cnt_zero += 1
                
        # 현재 칸이 아직 청소되지 않은 경우, 현재 칸 청소
        if room[r][c] == 0:
            room[r][c] = 2
            cnt += 1
        
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        elif cnt_zero == 0:
            # 후진 가능한 경우 후진
            if room[r - dx[d]][c - dy[d]] == 2:
                r -= dx[d]
                c -= dy[d]
            # 후진 불가능한 경우 작동 중지
            elif room[r - dx[d]][c - dy[d]] == 1:
                break

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        else:
            d -= 1 # 반시계 방향으로 90도 회전
            if d == -1:
                d = 3
            # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 전진
            if room[r + dx[d]][c + dy[d]] == 0:
                r += dx[d]
                c += dy[d]
            # 처음부터 다시 진행
            else:
                continue
        
    print(cnt)          

if __name__ == "__main__":
    main()

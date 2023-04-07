def main():
    n = int(input())
    mine_map = []
    answer_map = [['*' for _ in range(n)] for _ in range(n)]
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    mine_cnt = 0
    for _ in range(n):
        mine_map.append(list(map(str, input())))
                
    for i in range(n):
        for j in range(n):
            if mine_map[i][j] == '.':
                for k in range(8):    
                    x = i + dx[k]
                    y = j + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if mine_map[x][y] != '.':
                        mine_cnt += int(mine_map[x][y])
                answer_map[i][j] = mine_cnt
                mine_cnt = 0
                if answer_map[i][j] >= 10:
                    answer_map[i][j] = 'M'
        
    for i in range(n):
        print(*answer_map[i], sep='')
        
if __name__ == '__main__':
    main()

import sys
from typing import List, Tuple


'''
### 접근 방법
1. ( 물 위치 기록 -> 물 위치 옆에 있는 얼음 녹이기 -> 백조->백조 BFS ) 반복 [timeout]
2. ( 물 위치 기록 -> 물 위치 옆에 있는 얼음 녹이기 -> 물 위치 union-find -> 백조/백조 parent 동일하면 종료 ) 반복 [timeout]
3. ( 백조->백조 BFS -> 얼음을 만나면 queue에만 넣지 말고, 얼음 위치 기록 -> 기록해놓은 얼음 취이 모두 녹이고, visited 배열 유지한채로 bfs 재시작 ) 반복 [timeout]
4. DFS로 수정 [틀렸습니다.]
5. 4에서 녹이기 로직 잘못되어서 수정 [timeout]
6. 5에서 녹이기 로직 최적화
7. 시간 로직 오류 (백조 혼자 이동하지 않고, 물 위치에서 모두 녹이기 때문에 time // 2할 필요 없음) 성공
'''


if __name__ == "__main__":
    R, C = map(int, sys.stdin.readline().split())
    lake = []
    swans: List[Tuple[int, int]] = []
    waters = []
    for i in range(R):
        lake_row = []
        for j, element in enumerate(sys.stdin.readline().strip()):
            pos = (i, j)
            if element == ".":
                lake_row.append(element)
                waters.append(pos)
            if element == "X":
                lake_row.append(element)
            elif element == "L":
                swans.append(pos)
                waters.append(pos)
                lake_row.append(".")
        lake.append(lake_row)

    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[swans[0][0]][swans[0][1]] = True
    stack = [swans[0]]
    time = 0
    while True:
        # for r in lake:
        #     print(r)
        # print()
        # for r in visited:
        #     print(r)
        # print()
        # print()
        melted_ice = []
        while stack:
            i, j = stack.pop()
            for ii, jj in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                if 0 <= ii < R and 0 <= jj < C and not visited[ii][jj]:
                    if (ii, jj) == swans[1]:
                        print(time)
                        exit()
                    visited[ii][jj] = True
                    if lake[ii][jj] == ".":
                        stack.append((ii, jj))
                    else:
                        melted_ice.append((ii, jj))
        for ice in melted_ice:
            stack.append(ice)
            
        time += 1
        
        new_waters = []
        for water in waters:
            melted = False
            for ii, jj in [(water[0]-1, water[1]), (water[0], water[1]-1), (water[0], water[1]+1), (water[0]+1, water[1])]:
                if 0 <= ii < R and 0 <= jj < C and lake[ii][jj] == "X":
                    lake[ii][jj] = "."
                    melted = True
                    new_waters.append((ii, jj))
            if melted:
                new_waters.append(water)
        waters = new_waters
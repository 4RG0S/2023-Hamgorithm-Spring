import sys
from itertools import combinations

def main():
    N, M = map(int, sys.stdin.readline().split())
    city = [] # city[r][c] -> 0: 빈 칸, 1: 집, 2: 치킨집
    for _ in range(N):
        city.append(list(map(int, sys.stdin.readline().split())))
    
    house = [] # 집의 좌표 리스트
    chicken = [] # 치킨집의 좌표 리스트
    min_chicken_d = 2e9 # 도시의 치킨 거리의 최솟값
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i, j))
            elif city[i][j] == 2:
                chicken.append((i, j))
    
    # 치킨집 중 M개를 고르는 모든 경우의 수
    for i in combinations(chicken, M):
        d = [] # 치킨 거리 담는 리스트
        # 집 개수 만큼 반복
        for j in range(len(house)):
            d.append(2e9)
            # 치킨집 개수 만큼 반복
            for k in range(M):
                # i[k]치킨집 ~ house[j]집 사이 거리 계산
                # house[j]집에서 가장 가까운 치킨집까지의 거리
                d[j] = min(d[j], abs(house[j][0] - i[k][0]) + abs(house[j][1] - i[k][1]))
        # 최솟값 갱신
        if min_chicken_d > sum(d):
            min_chicken_d = sum(d)
    
    print(min_chicken_d)
    
if __name__ == "__main__":
    main()

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# visit을 사용하면 dfs만 사용하였을 때 이미 방문한 경로를 재방문하지 못하여 모든 탐색이 불가능하다.
# visit을 사요하지 않고 dfs만 사용하였을 때 모든 경로에 대해 탐색이 가능하지만 
# 중복 방문으로 인하여 탐색이 오래 걸려 시간 초과가 발생한다.
# dp를 이미 탐색한 경로의 재탐색을 막고 현재 경로의 갱신에 사용한다.
def main():
    m, n = map(int, input().split())
    zido = [list(map(int, input().split())) for _ in range(m)]
    # dp[x][y]는 x,y 좌표에서 경로의 끝까지의 경로의 개수
    # -1로 dp를 초기화 해주어 -1이면 탐색하지 않았음을 나타낸다.
    dp = [[-1 for j in range(n)] for i in range(m)]
    # 경로의 끝은 항상 방문하고 자기 자신임으로 경로가 1개
    dp[m-1][n-1] = 1
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # dfs를 사용하여 경로의 끝부터 경로를 탐색하여 dp를 갱신하여 준다.
    def dfs(x, y):
        # 이미 탐색한 좌표이면 재탐색을 막는다.
        # 탐색한 좌표의 값을 반환하여 준다.
        if dp[x][y] != -1:
            return dp[x][y]

        # 탐색하지 않았으면 0으로 초기화해준다.
        dp[x][y] = 0
        # x, y의 주변 좌표의 값을 활용하여 현재 좌표의 값을 얻는다.
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n\
                and zido[x][y] > zido[nx][ny] :
                dp[x][y] += dfs(nx, ny)
        # 현재 좌표의 값을 계산 후 반환한다.
        return dp[x][y]
    
    print(dfs(0, 0))
    
if __name__ == "__main__":
    main()
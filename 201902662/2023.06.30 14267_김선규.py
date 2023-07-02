from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    company = [[] for _ in range(n+1)]
    
    # 직속 상사가 가진 직속 부하 트리 형식으로 저장
    li = [0] + list(map(int, input().split()))
    for i in range(2, n+1):
        company[li[i]].append(i)
    
    # 직원이 받은 칭찬 저장, 여러 번 칭찬 받을 수 있음
    li = [0 for _ in range(n+1)]
    for _ in range(m):
        i, w = map(int, input().split())
        li[i] += w
    
    # 사장부터 시작하여 bfs로 모든 부하 직원을 순회한다.
    # 직속상사 순회 시 부하 직원의 칭찬 횟수에
    # 직속상사의 칭찬 횟수를 더해준다.
    que = deque([1])
    while que:
        v = que.popleft()
        for i in company[v]:
            li[i] = li[i] + li[v]
            que.append(i)
    print(*li[1:])
    
if __name__ == "__main__":
    main()
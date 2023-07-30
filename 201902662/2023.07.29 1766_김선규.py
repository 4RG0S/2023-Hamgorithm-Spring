import heapq
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input+().split())
    
    # i번 문제를 풀기 전 풀어야 하는 문제 수
    prev = [0 for _ in range(n+1)]
    # i번 문제를 풀어야 풀 수 있는 문제 저장
    prob = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        prev[b] += 1
        prob[a].append(b)
    
    # 문제 번호가 낮을수록 쉬워서 우선순위 큐에 담아 먼저 풀어 준다.
    que, ans = [], []
    
    # 문제를 풀기 전 풀어야 하는 문제가 없는 문제를 큐에 담는다.
    for i in range(1, n+1):
        if prev[i] == 0:
            heapq.heappush(que, i)
    
    # 큐에서 우선순위가 높은 문제를 꺼내서 정답배열에 담는다.
    # 해당 문제를 풀어야 쉽게 풀 수 있는 문제들을 순회하여
    # 풀 수 있으면 우선순위 큐에 넣어준다.
    while que:
        e = heapq.heappop(que)
        ans.append(e)
        for i in prob[e]:
            prev[i] -= 1
            if prev[i] == 0:
                heapq.heappush(que, i)
        
    print(*ans)
    
if __name__ == '__main__':
    main()
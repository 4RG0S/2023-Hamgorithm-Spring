import heapq
import sys
input = sys.stdin.readline

# 큐에서 최대(최소)가 다릅 큐에서 삭제되었는 지 확인
# 삭제 되었으면 그 값을 꺼내는 식으로 동기화
def sync(que):
    while que and not visit[que[0][1]]:
        heapq.heappop(que)

def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        
        # maxq와 minq에 원소가 삽입될 때 같은 순서로 삽입된다는 보장이 없음
        maxq = []
        minq = []
        visit = [False] * 1000001
        for i in range(k):
            op, n = input().split()
            if op == 'I':
                heapq.heappush(maxq, (-int(n), i))
                heapq.heappush(minq, (int(n), i))
                visit[i] = True
            else:
                if n == '1':
                    sync(maxq)
                    if maxq:
                        visit[maxq[0][1]] = False
                        heapq.heappop(maxq)
                else:
                    sync(minq)
                    if minq:
                        visit[minq[0][1]] = False
                        heapq.heappop(minq)
            
        sync(maxq)
        sync(minq)
        
        if maxq:
            print(-maxq[0][0], minq[0][0])
        else:
            print('EMPTY')
    
if __name__ == '__main__':
    main()
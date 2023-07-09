import heapq
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    # heap을 사용하여 점수 순서대로 정렬
    subject = []
    for _ in range(n):
        d, w = map(int, input().split())
        heapq.heappush(subject, (-w, d))
    
    # 해당 날에 수행할 과제의 점수를 저장할 배열
    day = [0] * 1001
    # 점수 순서대로 완전 탐색하며 해당 날에 수행하거나
    # 해당 날에 할 과제가 있으면 가까운 날에 수행하도록 함
    for _ in range(n):
        w, d = heapq.heappop(subject)
        for i in range(d, 0, -1):
            if day[i] == 0:
                day[i] = w
                break
    
    print(-sum(day))
    
if __name__ == "__main__":
    main()
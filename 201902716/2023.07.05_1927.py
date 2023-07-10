import sys
import heapq

def main():
    min_hq = [] # 최소 힙
    result = []
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        x = int(sys.stdin.readline()) # 입력
        r = 0 # 출력 초기 값 0
        if x == 0: # 입력이 0
            if len(min_hq) > 0: # 배열에 원소가 있으면
                r = heapq.heappop(min_hq) # 가장 작은 값 삭제
            result.append(r) # 가장 작은 값 or 0 저장
        else:
            heapq.heappush(min_hq, x) # 원소 삽입
    
    print(*result)
    
if __name__ == '__main__':
    main()

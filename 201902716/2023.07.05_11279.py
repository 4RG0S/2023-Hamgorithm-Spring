import sys
import heapq

def main():
    max_hq = [] # 최대 힙
    result = []
    N = int(sys.stdin.readline())
    
    for _ in range(N):
        x = int(sys.stdin.readline()) # 입력
        r = 0 # 출력 초기 값 0
        if x == 0: # 입력이 0
            if len(max_hq) > 0: # 배열에 원소가 있으면
                r = heapq.heappop(max_hq) # 가장 작은 값 (음수여서 절댓값이 가장 큰 값) 삭제
            result.append(-r) # 가장 큰 값 or 0 저장 (-붙여서 다시 양수로 변환)
        else:
            heapq.heappush(max_hq, -x) # 원소 삽입 (음수로 삽입하여 최대 힙 구현)
    
    print(*result)
    
if __name__ == '__main__':
    main()

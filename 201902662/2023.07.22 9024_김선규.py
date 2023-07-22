import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        # 이진 탐색을 할 수 있도록 배열을 입력받아 정렬한다.
        li = sorted(list(map(int, input().split())))
        
        # 모든 경우에 대해 탐색하며 탐색한 값과 k의 차이를 저장한다.
        # 차이가 작은 경우 cnt를 1로 초기화 하고 같으면 cnt를 1 증가한다.
        cnt, m = 0, float('Inf')
        for i in range(n-1):
            start = i+1; end = n-1
            while start <= end:
                mid = (start+end)//2
                tmp = k-(li[i] + li[mid])
                
                if abs(tmp) < m:
                    cnt = 1; m = abs(tmp)
                elif abs(tmp) == m:
                    cnt += 1
                
                if tmp < 0:
                    end = mid - 1
                else:
                    start = mid + 1
        print(cnt)
    
if __name__ == "__main__":
    main()
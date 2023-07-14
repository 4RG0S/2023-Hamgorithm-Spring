import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    # 차이를 구하기 위해 원소를 정렬해준다.
    li = sorted([int(input()) for _ in range(n)])
    
    # start는 구간의 시작점, end는 구간의 끝점.
    # start와 end를 0으로 초기화하고, end를 1씩 증가시키면서 차이가 m 이상이 되는지 확인
    # 차이가 n이상 되면 end의 증가를 멈추고 
    # 구간의 시작점인 start를 1씩 증가시키면서 탐색을 반복한다.
    end, dif = 0, 2000000000
    for start in range(n):
        while end != n and li[end] - li[start] < m:
            end += 1
        
        if end == n:
            break
        
        if li[end] - li[start] < dif:
            dif = li[end] - li[start]
        
    print(dif)
    
if __name__ == '__main__':
    main()
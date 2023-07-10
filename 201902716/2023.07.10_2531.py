def main():
    n, d, k, c = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    max_chobab = 0 # 최대 초밥 종류 초기화
    
    # 회전 초밥이므로, 인덱스 범위 나누어 연속된 k개 초밥 종류 수 구하기
    # 쿠폰 초밥 더해서 종류 수 구하기 (리스트 인덱싱, 집합 사용)
    for i in range(n):
        if (i + k) > n: 
            chobab = len(set(a[i:n] + a[0:(i+k)%n] + [c]))
        else:
            chobab = len(set(a[i:i+k] + [c]))
        max_chobab = max(max_chobab, chobab)
        
    print(max_chobab)
if __name__ == '__main__':
    main()

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    cnt, start, end = 0, 0, 0 # cnt, 투 포인터 start, end 0으로 초기화
    hap = a[0] # 부분합 초기화

    while start < n: # start가 수열 길이 보다 작은 동안 반복
        if hap < m: # 부분합이 m보다 작을 때, end +1
            if end == n - 1: # end가 마지막 인덱스면 탈출
                break
            else: 
                end += 1
                hap += a[end]
        elif hap > m: # 부분합이 m보다 클 때, start +1
            hap -= a[start]
            start += 1
        else: # 부분합이 m일 때, cnt +1, start +1
            cnt += 1
            hap -= a[start]
            start += 1
    print(cnt)

if __name__ == '__main__':
    main()

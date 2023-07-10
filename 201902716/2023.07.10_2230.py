def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)]
    a.sort() # 정렬해야 투 포인터 변화시, 두 수의 차가 커지고 작아짐 알 수 있음
    start, end = 0, 1 # 투 포인터 초기화
    min_cha = 2e9 # 두 수의 최소 차, 최댓값으로 초기화
    
    while start < n - 1:  # start가 마지막 인덱스 바로 앞일때 까지만 반복
        cha = a[end] - a[start] # 두 수의 차
        if cha >= m: # 두 수의 차가 m보다 크거나 같을 때, 최소 차 수정, start +1
            min_cha = min(min_cha, cha)
            start += 1
        elif cha < m: # 두 수의 차가 m보다 작을 때
            if end == n - 1: # end가 마지막 인덱스가 일 때, start +1
                start += 1
            else: # end가 마지막 인덱스가 아닐 때, end +1
                end += 1 
    print(min_cha)

if __name__ == '__main__':
    main()

def main():
    n, s = map(int, input().split())
    li = list(map(int, input().split()))
    
    # 누적합을 사용하여 구간의 합을 계산하기 쉽게 변환
    psum = [0]
    for i in range(n):
        psum.append(psum[-1]+li[i])
    
    # start는 구간의 시작점, end는 구간의 끝점
    # start와 end를 0으로 초기화하고, end를 1씩 증가시키면서 구간의 합이 s 이상이 되는지 확인
    # end가 n보다 커지면 구간의 합이 s 이상인 구간을 찾지 못한 것이므로 종료
    # 구간의 합이 s 이상이 되는 구간을 찾으면, 구간의 길이를 비교하여 최소 길이를 갱신
    end, m = 1, n+1
    for start in range(n+1):
        while end <= n and psum[end] - psum[start] < s:
            end += 1
        if end > n:
            break
        if psum[end] - psum[start] >= s and end-start < m:
            m = end-start
    
    # m이 n+1이면 구간의 합이 s 이상인 구간을 찾지 못한 것이므로 0 출력
    if m == n+1:
        print(0)
    else:
        print(m)
    
if __name__ == "__main__":
    main()
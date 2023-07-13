def main():
    n = int(input())
    
    prime = []
    isPrime = [False for _ in range(n+1)]
    
    # 에라토스테네스의 체를 사용하여 n보다 작은 소수를 구한다.
    for i in range(2, n+1):
        if isPrime[i]:
            continue
        prime.append(i)
        for j in range(i+i, n+1, i):
            isPrime[j] = True
    
    # 소수의 누적합을 구한다.
    psum = [0]
    for e in prime:
        psum.append(psum[-1] + e)
    
    # start는 구간의 시작점, end는 구간의 끝점
    # 누적합의 처음부터 탐색하여 연속된 소수의 합을 구한다.
    # 연속된 소수의 합이 n과 같으면 카운트를 증가한다.
    # 연속된 소수의 합이 n보다 크거나 같으면 현재 구간에서 최소임으로 break한다.
    # 구간의 시작점인 start를 1씩 증가시키면서 탐색을 반복한다.
    cnt = 0
    for start in range(len(psum)):
        for end in range(start, len(psum)):
            if psum[end] - psum[start] >= n:
                if psum[end] - psum[start] == n:
                    cnt += 1
                break
    print(cnt)
    
if __name__ == "__main__":
    main()
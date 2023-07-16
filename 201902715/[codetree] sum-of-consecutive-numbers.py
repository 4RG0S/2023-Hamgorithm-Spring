import sys


n: int
start: int # 연속된 자연수의 시작 (합에 포함)
end: int # 연속된 자연수의 끝 (합에 포함되지 않음)
cumulative_sum: int
result: int


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    start: int = 1
    end: int = 2

    cumulative_sum = 1

    result = 0

    while start <= n:
        if cumulative_sum == n:
            result += 1
            cumulative_sum -= start
            start += 1
            continue
        if cumulative_sum > n:
            cumulative_sum -= start
            start += 1
            continue
        if cumulative_sum < n:
            cumulative_sum += end
            end += 1
            continue

    print(result)

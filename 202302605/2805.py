import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(arr)

while left <= right:
    high = (left + right) // 2
    sum = 0
    sum2 = 0

    for i in arr:
        if i > high:
            sum += i - high
            sum2 += i - (high + 1)

    if sum < m:
        right = high - 1

    elif sum > m:
        if sum2 < m:
            print(high)
            break

        elif sum2 == m:
            print(high + 1)
            break

        else:
            left = high + 1

    else:
        print(high)
        break
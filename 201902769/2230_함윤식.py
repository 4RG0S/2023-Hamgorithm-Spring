import sys
n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()
start, end = 0, 0
diff = sys.maxsize
while end < n:
    if end < start:
        end += 1
    elif arr[end] - arr[start] >= m:
        diff = min(diff, arr[end] - arr[start])
        start += 1
    else:
        end += 1

print(diff)

# 0<= A[i] <= 1000000000의 조건이 주어지므로 end += 1 시 항상 값이 커지고 start += 1 시 값이 항상 작아진다.
# 따라서 투포인터를 활용해 문제를 해결할 수 있다.

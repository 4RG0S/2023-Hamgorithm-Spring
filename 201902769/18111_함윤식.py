import sys

n, m, b = map(int, input().split())
arr = []

for i in range(n):
    cur = list(map(int, input().split()))
    arr += cur

answer = sys.maxsize
idx = 0

for target in range(257):
    max_target, min_target = 0, 0

    for j in arr:
        if j >= target:
            max_target += j - target
        else:
            min_target += target - j

    if max_target + b >= min_target:
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2)
            idx = target

print(answer, idx)

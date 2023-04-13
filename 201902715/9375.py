import sys
from collections import defaultdict


T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cloth_dict = defaultdict(lambda: 1)
    for _ in range(N):
        _, cloth_type = sys.stdin.readline().split()
        cloth_dict[cloth_type] += 1
    result = 1
    for key in cloth_dict:
        result *= cloth_dict[key]
    result -= 1
    print(result)

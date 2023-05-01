from collections import Counter
import math
N = int(input())
N_list = list(map(int, input().split()))
res = []
sorted_N_list = sorted(N_list)

for i in N_list:
    res.append(sorted_N_list.index(i))
    sorted_N_list[sorted_N_list.index(i)] = math.inf
print(*res)

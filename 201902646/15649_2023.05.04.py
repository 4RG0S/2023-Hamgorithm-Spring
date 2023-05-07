from sys import stdin
from itertools import permutations
N, M = map(int, stdin.readline().split())
lst = list(map(str, range(1, N+1)))
print('\n'.join(list(map(' '.join, permutations(lst, M)))))

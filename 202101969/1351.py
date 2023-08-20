import sys
from collections import defaultdict

def find_num(n):
    if hash[n] != 0:
        return hash[n]
    else:
        hash[n] = find_num(n//P) + find_num(n//Q)
    return hash[n]

N,Q,P = map(int, sys.stdin.readline().split())
hash = defaultdict(int)
hash[0] = 1

print(find_num(N))
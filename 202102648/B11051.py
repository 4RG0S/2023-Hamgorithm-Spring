import sys
from math import factorial

input = sys.stdin.readline
n, k = map(int, input().split())

ans = factorial(n) // (factorial(k) * factorial(n-k))

print(ans % 10007)
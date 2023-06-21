import sys
a, b = map(int, sys.stdin.readline().split())
set_a = set(map(int, sys.stdin.readline().split()))
set_b = set(map(int, sys.stdin.readline().split()))
a_b = len(set_a - set_b)
b_a = len(set_b - set_a)
print(a_b + b_a)
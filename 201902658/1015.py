import sys
import math

A_size = int(sys.stdin.readline())
A = sys.stdin.readline().replace("\n", "").split(' ')
A = [int(i) for i in A]

sorted_A = [i for i in A]
sorted_A.sort()

P = []

for i in A:
    P.append(sorted_A.index(i))
    sorted_A[sorted_A.index(i)] = -1

results = [i for i in P]

for result in results:
    sys.stdout.write(str(result)+' ')
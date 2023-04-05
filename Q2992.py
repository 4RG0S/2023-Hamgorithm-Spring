from itertools import permutations
from math import inf

X = input()
min = inf
for i in permutations(X,len(X)):
    str = ''
    for j in i:
        str += j
    if min > int(str) and int(X)< int(str):
        min = int(str)
if min == inf:
    print(0)
else:
    print(min)

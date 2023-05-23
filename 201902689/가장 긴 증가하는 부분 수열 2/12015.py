from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())

sequences = list(map(int, input().split(' ')))
lis = [sequences[0]]

for index, num in enumerate(sequences[1:]):
    if num < lis[-1]:
        tmp = bisect_left(lis, num)
        lis[tmp] = num
    elif num > lis[-1]:
        lis.append(num)
print(len(lis))

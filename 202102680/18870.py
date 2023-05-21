import sys
N = input()
arr = list(map(int,sys.stdin.readline().split()))

arr1 = list(sorted(set(arr)))
dic = {arr1[i]: i for i in range(len(arr1))}
for i in arr:
    print(dic[i], end=" ")
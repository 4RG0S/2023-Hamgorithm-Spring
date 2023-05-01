import sys
n = int(input())
temp = list(map(int,sys.stdin.readline().split()))
result = []
result.append([0,0])
for i in range(n):
    result.append([i,temp[i]])

result.sort(key = lambda x : x[1])
sum = 0
d = []
d.append(0)
d.append(result[1][1])
sum += result[1][1]
for i in range(2,n+1):
    d.append(d[i-1]+result[i][1])
    sum += d[i]

print(sum)
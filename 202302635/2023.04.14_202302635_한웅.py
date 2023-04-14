import sys
N =int(input())
data = list(map(int,sys.stdin.readline().rstrip()))
sum = 0
for i in range(N) :
    sum += int(data[i])
print(sum)
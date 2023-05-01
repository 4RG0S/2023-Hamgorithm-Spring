n = int(input())
time = list(map(int, input().split()))
result = 0
time.sort()

for i in range(1, n+1):
    result += sum(time[0:i])
    
print(result)

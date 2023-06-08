def round2(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    
    else:
        return int(n)

n = int(input())

if n== 0:
    print(0)
    exit(0)

arr = []
sum=0
for i in range(n):
    arr.append(int(input()))
    sum+=arr[i]

arr = sorted(arr)

x = round2(n*0.15)
for i in range(x):
    sum -= arr[i] + arr[n-i-1]

average = round2(sum / (n-x*2))

print(average)
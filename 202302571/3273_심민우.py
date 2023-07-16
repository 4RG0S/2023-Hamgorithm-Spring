# 23.07.16
# BOJ 3279
# 투 포인터

n = int(input())

arr = list(map(int, input().split()))
arr = sorted(arr)

x = int(input())

tot = 0
start=0
end= n-1

while(start<end):
    if arr[end] + arr[start] == x:
        tot +=1
        end -=1
        start +=1
    elif arr[end] + arr[start] > x:
        end-=1
    else:
        start+=1

print(tot)
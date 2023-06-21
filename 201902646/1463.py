num = int(input())
cnt = [0]*(num+1)

for i in range(2,num+1):
    cnt[i]=cnt[i-1]+1
    if i%2 == 0:
        cnt[i] = min(cnt[i], cnt[i//2]+1)
    if i%3 == 0:
        cnt[i] = min(cnt[i], cnt[i//3]+1)

print(cnt[num])

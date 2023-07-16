num, S = map(int, input().split())
arr = list(map(int, input().split()))

st, en = 0, 0
sum = arr[0]
ans = 100001

while True:
    if sum < S:
        en += 1
        if en == num:
            break
        sum += arr[en]
    else:
        sum -= arr[st]
        ans = min(ans, en - st + 1)
        st += 1

if ans == 100001:
    print(0)
else:
    print(ans)

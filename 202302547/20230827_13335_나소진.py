n, w, l = map(int, input().split())
arr = list(map(int, input().split()))
bridge = [0] * w
cnt = 0

while bridge:
  cnt += 1
  bridge.pop(0)

  if arr:
    if sum(bridge) + arr[0] > l:
      bridge.append(0)
    else:
      bridge.append(arr.pop(0))

print(cnt)

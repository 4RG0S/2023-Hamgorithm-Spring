a, b = list(map(int, input().split()))

input_list = []

for i in range(a):
  length = int(input())
  input_list.append(length)

start = 1;
end = max(input_list)

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in range(a):
        cnt += input_list[i] // mid
    if cnt >= b:
        start = mid + 1
    else:
        end = mid - 1
print(end)
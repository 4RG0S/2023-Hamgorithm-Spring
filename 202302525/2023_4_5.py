n = int(input())
arr = input().split()
result = [0]*n
order = 0

for i in range(n):
    low = 1001
    low_index = -1

    for i in range(n):
        arr[i] = int(arr[i])

        if arr[i] < low:
            low = arr[i]
            low_index = i

    result[low_index] = order
    arr[low_index] = 1001
    order += 1

print(*result)
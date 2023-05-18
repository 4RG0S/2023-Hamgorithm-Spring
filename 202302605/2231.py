n = int(input())

for i in range(n):
    st = str(i)
    arr = list(st)

    for j in range(len(arr)):
        arr[j] = int(arr[j])
    
    result = i + sum(arr)
    
    if result == n:
        print(i)
        break
    
    elif i == n-1:
        print(0)

    else:
        continue
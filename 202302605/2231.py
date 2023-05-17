n = int(input())

for i in range(n):
    st = str(i)
    arr = list(st)

    for j in range(len(arr)):
        arr[j] = int(arr[j])
    
    print(arr)
    result = i + sum(arr)
    
    if result == n:
        print(i)
        break
    
    else:
        continue
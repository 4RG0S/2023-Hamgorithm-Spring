n = int(input())
table1 = list(map(int, input().split()))
m = int(input())
table2 = list(map(int, input().split()))
table1.sort()

for i in table2:
    start = 0
    end = n-1
    key = False

    while start <= end:
        mid = (start + end)//2
        if i == table1[mid]:
            key = True
            break
        elif i <= table1[mid]:
            end = mid-1
        else:
            start = mid + 1
    
    if key:
        print(1)
    else:
        print(0)
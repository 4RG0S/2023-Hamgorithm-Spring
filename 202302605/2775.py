T = int(input())

arr = [[0 for i in range(14)] for j in range(15)]

for i in range(14):
    arr[14][i] = i+1
    arr[i][0] = 1

for i in range(14):
    for j in range(13):
        arr[13-i][j+1] = arr[13-i][j] + arr[14-i][j+1]

for i in range(15):
    for j in range(14):
        print(arr[i][j], end=' ')
    print()
          
for i in range(T):
    floor = int(input())
    ho = int(input())

    print(arr[14-floor][ho-1])
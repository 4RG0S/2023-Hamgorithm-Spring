n, m = map(int, input().split())

arr = [[] for i in range(n)]
ar = [[] for i in range(8)]

result = 0
last = 33

for i in range(n):
    st = input()
    arr[i] = list(st)

for i in range(n-7):
    for j in range(m-7):
        count = 0   # 첫번째 칸이 흰색인 경우
        count2 = 0  # 첫번째 칸이 검은색인 경우

        for k in range(8):
            ar[k] = arr[k+i][j:j+8]

        for a in range(8):
            for b in range(8):
                
                if (a+b) % 2 == 0:
                    if ar[a][b] == 'B':
                        count += 1
                    
                    if ar[a][b] == 'W':
                        count2 += 1

                else:
                    if ar[a][b] == 'B':
                        count2 += 1
                    
                    if ar[a][b] == 'W':
                        count += 1

        result = min(count, count2)
        last = min(last, result)

print(last)
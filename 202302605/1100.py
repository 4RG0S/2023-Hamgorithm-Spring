arr = [[] for i in range(8)]
count = 0

for i in range(8):
    st = input()
    arr[i] = list(st)

for a in range(8):
    for b in range(8):
        if (a + b) % 2 == 0:
            if arr[a][b] == 'F':
                count += 1

print(count)
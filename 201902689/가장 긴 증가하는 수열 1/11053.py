N = int(input())
sequences = list(map(int, input().split(' ')))
lis = [sequences[0]]
records = [0]
length = [0 for _ in range(N)]

for i in range(N):
    length[i] = 1
    for j in range(i):
        if sequences[i] > sequences[j]:
            length[i] = max(length[i], length[j] + 1)
print(max(length))
N, B, H, W = map(int, input().split())
cost = []
hotel = []
total = []
for i in range(H):
    cost.append(int(input()))
    hotel.append(list(map(int, input().split())))

for i in range(H):
    for j in hotel[i]:
        if j > N:
            total.append(N * cost[i])

if len(total) == 0:
    print('stay home')
elif min(total) > B:
    print('stay home')
else:
    print(min(total))


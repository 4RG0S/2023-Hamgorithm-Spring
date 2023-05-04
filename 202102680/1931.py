from sys import stdin
n = int(stdin.readline())

room = []
for _ in range(n):
    a,b = list(map(int,stdin.readline().split()))
    room.append([a,b])

room.sort(key = lambda x: (x[1], x[0]))

count = 1
end = room[0][1]
for i in range(1,n):
    if room[i][0] >= end:
        end = room[i][1]
        count +=1

print(count)

N = int(input())
li = []
for _ in range(N):
    S = input()
    count = 0
    for s in S:
        if 48 <= ord(s) <= 57:
            count += int(s)
    li.append([S, count])

li = sorted(li, key=lambda x: (len(x[0]), x[1], x[0]))
#print(li)
for i in range(N):
    print(li[i][0])

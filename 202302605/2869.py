up, down, high = map(int, input().split())

remain = high - up

day = remain / (up - down)

if day != int(day):
    day = int(day + 1)
else:
    day = int(day)

if remain <= 0:
    print(1)
else:
    print(day + 1)
high = [0, 0]

for i in range(9):
    n = int(input())
    if high[0] < n:
        high[0] = n
        high[1] = i

print(high[0])
print(high[1]+1)
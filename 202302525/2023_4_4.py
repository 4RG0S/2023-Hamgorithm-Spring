min, max = map(int, input().split())
table = [1] * 1_000_002  #0 ~ 1_000_001
prime = []
result = [1]*(max-min+1)
a = []

for i in range(2, 1_000_002):
    if i**2 > max:
        break
    elif table[i] == 1:
        prime.append(i)
        for j in range(i*2, 1_000_002, i):
            table[j] = 0

for i in prime:
    for j in range(i**2 * int(min/i**2),max+1 ,(i**2)):
        if j-min < 0 or result[j-min] == 0:
            continue
        a.append(j)
        result[j-min] = 0

print(max-min+1-len(a))
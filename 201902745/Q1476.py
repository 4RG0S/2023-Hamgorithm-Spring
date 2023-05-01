E1, S1, M1 = map(int, input().split())
e, s, m = 1, 1, 1
result = 1
while True:
    if e == E1 and s == S1 and m == M1:
        break
    e += 1
    s += 1
    m += 1
    result += 1
    if e >= 16:
        e -= 15
    if s >= 29:
        s -= 28
    if m >= 20:
        m -= 19
print(result)

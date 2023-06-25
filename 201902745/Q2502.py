import sys
d, k = map(int, input().split())

a, b = 1, 1
for _ in range(4, d + 1):
    a, b = b, a + b
a_c = 1
b_c = 0
while True:
    tmp = k - a * a_c
    if tmp < 0:
        break

    if tmp % b == 0:
        b_c = tmp // b
        break
    # print(a_c, b_c)
    a_c += 1

print(a_c)
print(b_c)

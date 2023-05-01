n = int(input())
a = input().split()
b = input().split()
result = 0

for i in range(n):
    a[i] = int(a[i])
    b[i] = int(b[i])

a.sort()
sorted_b = sorted(b)
new_a = [0] * n

for i in range(n):
    idx = b.index(sorted_b[i])
    new_a[idx] = a[-(i+1)]
    result += new_a[idx] * b[idx]
    b[idx] = ""

print(result)
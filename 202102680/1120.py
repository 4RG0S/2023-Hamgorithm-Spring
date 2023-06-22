a, b = input().split()

result = []
for i in range(len(b)-len(a)+1):
    count = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            count += 1
    result.append(count)

print(min(result))
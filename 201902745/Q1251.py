W = input()
result = []

for i in range(1, len(W)):
    for j in range(i + 1, len(W)):
        case1 = W[:i][::-1]
        case2 = W[i:j][::-1]
        case3 = W[j:][::-1]
        result.append(case1 + case2 + case3)
#print(result)
print(sorted(result)[0])

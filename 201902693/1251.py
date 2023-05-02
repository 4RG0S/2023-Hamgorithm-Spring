s = input()
result = []
for i in range(1, len(s) - 1) :
    for j in range(i + 1, len(s)) :
        s1 = s[0:i]
        s2 = s[i:j]
        s3 = s[j:len(s)]
        result.append(s1[::-1] + s2[::-1] + s3[::-1])

print(sorted(result)[0])
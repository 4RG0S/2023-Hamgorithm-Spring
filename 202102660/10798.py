words = [
    list(input())
    for _ in range(5)
]
max_len = 0

for i in range(5):
    if len(words[i]) > max_len:
        max_len = len(words[i])

result = ["" for _ in range(max_len)]

for i in range(5):  
    for j in range(len(words[i])):
        result[j] += words[i][j]

print("".join(result))
    

n = int(input())
word = list(map(str, input().split()))
word2 = []
for i in range(n-1):
    word.append(input())
word.sort()
word.sort(key=len)
for i in word:
    if i not in word2:
        word2.append(i)

for i in range(len(word2)):
    print(word2[i])

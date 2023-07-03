num = int(input())
count = 0

for i in range(num):
    lst = []
    word = input()
    for j in range(len(word)):
        if j > 0:
            if (word[j] in lst) and (word[j] != word[j - 1]):
                count -= 1
                break
        lst.append(word[j])
    count += 1

print(count)
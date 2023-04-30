document = input()
word = input()

count = 0
index = 0

for i in range(len(document)):
    if index > i:
        continue
    if word == document[i : i + len(word)]:
        count += 1
        index = i + len(word)

print(count)

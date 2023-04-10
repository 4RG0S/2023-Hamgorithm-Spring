from collections import defaultdict
result = defaultdict(int)

total_card = int(input())
cards = list(map(int, input().split(' ')))
find_card = int(input())
find_cards = list(map(int, input().split(' ')))

string = []
for i in cards:
    result[i] += 1

for i in find_cards:
    string.append(result[i])

print(" ".join(str(item) for item in string))

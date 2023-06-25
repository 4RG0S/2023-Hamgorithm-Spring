n = int(input())

for _ in range(n):
    ox = list(input())
    score = 0
    sum = 0
    for elem in ox:
        if elem == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)
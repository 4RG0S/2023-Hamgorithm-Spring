X = int(input())
X_num = [64, 32, 16, 8, 4, 2, 1]
count = 0
while X > 0:
    for target in X_num:
        if X // target == 1:
            count += 1
            X -= target
            break
print(count)

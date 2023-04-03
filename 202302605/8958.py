T = int(input())

for i in range(T):
    x = input()
    score = 0
    total = 0

    for i in range(len(x)):
        
        if x[i] == 'O':
            score = score + 1
            total = total + score
        
        else:
            score = 0

    print(total)
        

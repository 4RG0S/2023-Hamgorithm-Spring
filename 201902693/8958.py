a = int(input())
input_list = list(input() for _ in range(a))

x = 0
score = []

for i in range(len(input_list)) :
    for j in range(len(input_list[i])) :
        if input_list[i][j] == 'O' :
            x += 1
            score.append(x)
            
        elif input_list[i][j] == 'X' :
            x = 0
            
        if j + 1 == len(input_list[i]) :
            print(sum(score))
            score = []
            x = 0
if __name__ == "__main__":
    N = int(input())
    calc = [[0, []]  for _ in range(N + 1)]
    calc[1][0] = 0
    calc[1][1] = [1]
    
    for i in range(2, N + 1):
        calc[i][0] = calc[i - 1][0] + 1
        calc[i][1] = calc[i - 1][1] + [i]
        if i % 3 == 0 and calc[i // 3][0] + 1 < calc[i][0]:
            calc[i][0] = calc[i // 3][0] + 1
            calc[i][1] = calc[i // 3][1] + [i]
        if i % 2 == 0 and calc[i // 2][0] + 1 < calc[i][0]:
            calc[i][0] = calc[i // 2][0] + 1
            calc[i][1] = calc[i // 2][1] + [i]
       
    print(calc[N][0])
    print(*reversed(calc[N][1]))
if __name__ == "__main__":
    N = int(input())
    calc = [0] * (N + 1)
    
    for i in range(2, N + 1):
        calc[i] = calc[i - 1] + 1
        if i % 3 == 0:
            calc[i] = min(calc[i], calc[i // 3] + 1)
        if i % 2 == 0:
            calc[i] = min(calc[i], calc[i // 2] + 1)
    
            
    print(calc[N])
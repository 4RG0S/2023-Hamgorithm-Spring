def main():
    N, K = map(int, input().split())
    circle = [i+1 for i in range(N)]
    answer = []
    i = 0
    
    while circle:
        i = (i + K - 1) % len(circle)
        answer.append(circle.pop(i))
            
    print("<" + ", ".join(map(str, answer)) + ">")
            
if __name__ == '__main__':
    main()

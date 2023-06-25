def main():
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    answer = 0
    
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                card_sum = cards[i] + cards[j] + cards[k]
                if card_sum <= M:
                    answer = max(answer, card_sum)
    print(answer)

if __name__ == '__main__':
    main()

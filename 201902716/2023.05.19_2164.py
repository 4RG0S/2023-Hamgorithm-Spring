from collections import deque

def main():
    N = int(input())
    cards = deque(range(1, N+1))

    while len(cards) > 1:
        cards.popleft()
        cards.append(cards.popleft())

    print(cards[0])

if __name__ == '__main__':
    main()

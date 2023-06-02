import sys
from collections import Counter

def main():
    N = int(sys.stdin.readline())
    cards = Counter(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline())
    f_cards = list(map(int, sys.stdin.readline().split()))

    answer = []
    
    for f_card in f_cards:
        if f_card in cards.keys():
            answer.append(cards[f_card])
        else:
            answer.append(0)
    print(*answer)
        
if __name__ == '__main__':
    main()

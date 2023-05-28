def main():
    N = int(input())
    people = []
    ranks = []
    
    for _ in range(N):
        w, h = map(int, input().split())
        people.append((w, h))

    for i in people:
        rank = 1
        for j in people:
            if i != j and i[0] < j[0] and i[1] < j[1]:
                rank += 1
        ranks.append(rank)
    
    print(*ranks)
        
if __name__ == '__main__':
    main()

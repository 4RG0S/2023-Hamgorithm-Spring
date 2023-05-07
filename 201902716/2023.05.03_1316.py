def main():
    r = []
    N = int(input())
    cnt = N
    
    for _ in range(N) :
        word = input()
        for i in range(1, len(word)):
            if word[i-1] not in r:
                r.append(word[i-1])
            if word[i-1] != word[i] and word[i] in r:
                cnt -= 1
                break
        r = []       
    print(cnt)
    
if __name__ == '__main__':
    main()

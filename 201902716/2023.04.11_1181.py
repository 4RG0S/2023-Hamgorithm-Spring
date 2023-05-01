def main():
    words = []
    n = int(input())
    for _ in range(n):
        word = input()
        if word not in words:
            words.append(word) 
             
    words = sorted(words, key = lambda x: (len(x), x))

    for word in words:
        print(word)
        
if __name__ == '__main__':
    main()

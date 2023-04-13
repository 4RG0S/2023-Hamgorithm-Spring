def main():
    word = input()
    n = len(word)
    dictionary = []

    for i in range(1, n-1):
        for j in range(1, n-i):
            dictionary.append(word[:i][::-1] + word[i:i+j][::-1] + word[i+j:][::-1])

    print(min(dictionary))
        
if __name__ == '__main__':
    main()

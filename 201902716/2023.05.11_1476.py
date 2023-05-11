def main():
    E, S, M = map(int, input().split())
    y = 1

    while True:
        if (y - E) % 15 == 0 and (y - S) % 28 == 0 and (y - M) % 19 == 0:
            break
        y += 1
    print(y)
    
if __name__ == '__main__':
    main()

def main():
    N = int(input())
    cnt = 0
    num = 666
    
    while True:
        if '666' in str(num):
            cnt += 1
            if cnt == N:
                print(num)
                break
        num += 1

if __name__ == '__main__':
    main()

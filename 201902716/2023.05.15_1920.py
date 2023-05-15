def main():
    N = int(input())
    A = set(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    result = []
    for i in B:
        if i in A:
            result.append(1)
        else:
            result.append(0)
    print(*result)

if __name__ == '__main__':
    main()

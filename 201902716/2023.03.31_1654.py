def main():
    K, N = map(int, input().split())

    lan_cables = []
    for _ in range(K):
        lan_cables.append(int(input()))

    left, right = 1, max(lan_cables)

    while left <= right:
        mid = (left + right) // 2
        count = 0
        for cable in lan_cables:
            count += cable // mid
        if count >= N:
            left = mid + 1
        else:
            right = mid - 1

    print(right)
        
if __name__ == '__main__':
    main()

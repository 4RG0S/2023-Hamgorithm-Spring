def main():
    N = int(input())
    cnt = 0
    
    if len(str(N)) <= 2:
        cnt += N
    else:
        cnt += 99
        for i in range(100, N+1):
            d_list = []
            for j in range(len(str(i))-1):
                d_list.append(int(str(i)[j+1]) - int(str(i)[j]))
            if max(d_list) == min(d_list):
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()

def main():
    n = input()
    cnt = [0]*10
    
    for i in n:
        cnt[int(i)] += 1
    x = [int((cnt[6]+cnt[9]+1)/2)]
    cnt[6], cnt[9] = 0, 0
    print(max(cnt + x))
        
if __name__ == '__main__':
    main()

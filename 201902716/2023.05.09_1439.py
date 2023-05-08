def main():
    s = input()
    cnt = [0, 0]
    prev = s[0]
    
    for i in s[1:]:
        if i != prev:
            cnt[int(prev)] += 1
            prev = i
        else:
            continue
    cnt[int(s[-1])] += 1
    print(min(cnt))
    
if __name__ == '__main__':
    main()

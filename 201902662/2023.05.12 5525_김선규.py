def main():
    n, m, s = int(input()), int(input()), input()
    
    p_li = []
    current = 0
    if s[0] == "I":
        current = 1
    for i in range(m-1):
        if s[i] == s[i+1]:
            if s[i] == "I":
                if current > 2:
                    p_li.append(current)
                current = 1
            else:
                if current > 2:
                    p_li.append(current-1)
                current = 0
        else:
            current += 1
    
    if current > 2 and s[-1] != s[-2]:
        p_li.append(current)
    
    ans = 0
    for i in p_li:
        r = int((i-1)/2) - n + 1
        if r > 0:
            ans += r
    print(ans)
    
if __name__ == '__main__':
    main()
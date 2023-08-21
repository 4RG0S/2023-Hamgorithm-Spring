def main():
    s = input()
    n = len(s)
    dic = {}
    for i in range(n):
        dic[s[i]] = i+1
    
    s = input()
    acc = 1
    num = 0
    for i in range(len(s)-1, -1, -1):
        num = (dic[s[i]] * acc + num) % 900528
        acc = (acc * n) % 900528
    
    print(num)
        
if __name__ == "__main__":
    main()
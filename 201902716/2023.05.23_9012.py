def main():
    N = int(input())
    
    for _ in range(N):
        ps = input()
        cnt = 0
        for i in ps:
            if cnt < 0:
                break
            if i == "(":
                cnt += 1
            else:
                cnt -= 1
            
        answer = "YES" if cnt == 0 else "NO"
        print(answer)
        
if __name__ == '__main__':
    main()

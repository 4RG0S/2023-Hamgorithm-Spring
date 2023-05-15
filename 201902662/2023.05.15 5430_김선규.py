def main():
    T = int(input())
    for _ in range(T):
        p = input()
        n = int(input())
        li = input()
        if len(li) == 2:
            li = []
        else:
            li = li[1:len(li)-1].split(",")
            
        state, start, end = True, 0, n
        for i in range(len(p)):
            if p[i] == 'R':
                state = not state
            else:
                if state:
                    start += 1
                else:
                    end -= 1
        
        if end < start:
            print("error")
        else:
            if state:
                print('['+','.join(li[start: end])+']')
            else:
                print('['+','.join(li[start: end][::-1])+']')
    
if __name__ == '__main__':
    main()
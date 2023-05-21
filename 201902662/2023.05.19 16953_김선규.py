from collections import deque

def main():
    a, b = list(map(int, input().split()))
    
    que = deque([(a, 1)])
    count = -1
    while que:
        n, c = que.popleft()
        
        if n == b:
            count = c
            break
        elif n > b:
            continue
        
        next_c = c+1
        que.append((n*2, next_c))
        que.append((n*10+1, next_c))
    
    print(count)
    
if __name__ == "__main__":
    main()
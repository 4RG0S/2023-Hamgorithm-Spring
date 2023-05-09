N, M = map(int, input().split())

def re(result):
    if len(result) == M:
        print(*result)
        return
        
    for i in range(1, N+1):
        if len(result) != 0:
            if i <= result[-1]:
                continue
            
        result.append(i)
        re(result)
        result.pop()
    
re([])
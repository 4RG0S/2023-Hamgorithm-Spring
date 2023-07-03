if __name__ == "__main__":
    N, K = map(int, input().split())
    num = list(map(int, input().strip()))
    stack = []
    
    del_num = K
    
    for i in range(N):
        while del_num > 0 and stack:
            if stack[len(stack) - 1] < num[i]:
                stack.pop()
                del_num -= 1
            else:
                break
        stack.append(num[i])
    
    result = ""
    
    for i in range(N - K):
        result += str(stack[i])
    print(result)
    
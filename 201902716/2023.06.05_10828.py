def main():
    N = int(input())
    stack = []
    results = []
    size = 0

    for _ in range(N):
        command = list(map(str, input().split()))
        if command[0] == 'push':
            stack.append(int(command[1]))
            size += 1
        elif command[0] == 'pop':
            if size == 0:
                results.append(-1)
            else:
                results.append(stack.pop())
                size -= 1
        elif command[0] == 'size':
            results.append(size)
        elif command[0] == 'empty':
            results.append(1 if len(stack) == 0 else 0) 
        elif command[0] == 'top':
            results.append(-1 if len(stack) == 0 else stack[-1])

    print(*results)
            
if __name__ == '__main__':
    main()

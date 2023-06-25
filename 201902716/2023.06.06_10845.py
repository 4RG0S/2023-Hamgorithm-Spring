def main():
    N = int(input())
    queue = []
    results = []
    size = 0

    for _ in range(N):
        command = list(map(str, input().split()))
        if command[0] == 'push':
            queue.append(int(command[1]))
            size += 1
        elif command[0] == 'pop':
            if size == 0:
                results.append(-1)
            else:
                results.append(queue.pop(0))
                size -= 1
        elif command[0] == 'size':
            results.append(size)
        elif command[0] == 'empty':
            results.append(1 if size == 0 else 0) 
        elif command[0] == 'front':
            results.append(-1 if size == 0 else queue[0])
        elif command[0] == 'back':
            results.append(-1 if size == 0 else queue[-1])
            
    print(*results)
            
if __name__ == '__main__':
    main()

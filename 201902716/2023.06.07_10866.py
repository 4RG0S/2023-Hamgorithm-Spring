import sys

def main():
    N = int(sys.stdin.readline())
    deque = []
    results = []
    size = 0

    for _ in range(N):
        command = list(map(str, sys.stdin.readline().split()))
        if command[0] == 'push_front':
            deque.insert(0, int(command[1]))
            size += 1
        elif command[0] == 'push_back':
            deque.append(int(command[1]))
            size += 1
        elif command[0] == 'pop_front':
            if size == 0:
                results.append(-1)
            else:
                results.append(deque.pop(0))
                size -= 1
        elif command[0] == 'pop_back':
            if size == 0:
                results.append(-1)
            else:
                results.append(deque.pop())
                size -= 1
        elif command[0] == 'size':
            results.append(size)
        elif command[0] == 'empty':
            results.append(1 if size == 0 else 0) 
        elif command[0] == 'front':
            results.append(-1 if size == 0 else deque[0])
        elif command[0] == 'back':
            results.append(-1 if size == 0 else deque[-1])
            
    print(*results)
            
if __name__ == '__main__':
    main()

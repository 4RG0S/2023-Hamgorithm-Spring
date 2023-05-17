import sys

def main():
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(sys.stdin.readline()))
    print(*sorted(numbers))

if __name__ == '__main__':
    main()

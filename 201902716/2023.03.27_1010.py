import math

def main():
    case = int(input())
    for _ in range(case):
        n, m = map(int, input().split(' '))
        bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
        print(bridge)
    
if __name__ == '__main__':
    main()
    

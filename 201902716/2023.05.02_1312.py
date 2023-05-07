def main():
    A, B, N = map(int, input().split())
    
    for _ in range(N) :
        A = (A % B) * 10
        q = A // B
    print(q)
    
if __name__ == '__main__':
    main()

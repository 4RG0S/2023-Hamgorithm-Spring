def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort(reverse=True)
    
    for i in range(n):
        a[i] *= b[i]
        
    print(sum(a))
    
if __name__ == '__main__':
    main()


def main():
    a, b, c = list(map(int, input().split()))
    
    def multi(v, n):
        if n == 1:
            return v % c
        
        rec = multi(v, n//2)
        if n % 2 == 0:
            return (rec * rec) % c
        else:
            return (rec * rec * v) % c
        
    print(multi(a, b))    
        
if __name__ == "__main__":
    main()
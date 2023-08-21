def main():
    n, p, q, x, y = map(int, input().split())
    a = {0 : 1}
    def fun(num):
        try:
            return a[num]
        except:
            a[num] = fun(num//p) + fun(num//q)
            return a[num]
    print(fun(n))
    
if __name__ == "__main__":
    main()
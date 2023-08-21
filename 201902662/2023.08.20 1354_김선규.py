def main():
    n, p, q, x, y = map(int, input().split())
    a = {}
    def fun(num):
        if num > 0:
            try:
                return a[num]
            except:
                a[num] = fun(num//p-x) + fun(num//q-y)
                return a[num]
        return 1
    print(fun(n))
    
if __name__ == "__main__":
    main()
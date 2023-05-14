import sys
input = sys.stdin.readline

def main():
    n = int(input())
    image = [input() for _ in range(n)]
    
    def fun(i, j, n):
        if n == 1:
            return image[i][j]
        else:
            h = int(n/2)
            s = fun(i, j, h) + fun(i, j+h, h) + fun(i+h, j, h) + fun(i+h, j+h, h)
            if s == "0000" or s == "1111":
                return s[0]
            else:
                return "(" + s + ")"
            
    print(fun(0, 0, n))
    
if __name__ == '__main__':
    main()
def main():
    n = int(input())
    k = int(n / 3)
    matrix = [[" " for j in range(5*k+k-1)] for i in range(n)]
    def star(i, j, n):
        if n == 3:
            matrix[i][j] = "*"
            matrix[i+1][j-1] = "*"
            matrix[i+1][j+1] = "*"
            matrix[i+2][j-2] = "*"
            matrix[i+2][j-1] = "*"
            matrix[i+2][j] = "*"
            matrix[i+2][j+1] = "*"
            matrix[i+2][j+2] = "*"
        else:
            next_n = int(n/2)
            star(i, j, next_n)
            star(i+next_n, j-next_n, next_n)
            star(i+next_n, j+next_n, next_n)
    star(0, n-1, n)
    for i in matrix:
        print(''.join(i))
    
if __name__ == "__main__":
    main()
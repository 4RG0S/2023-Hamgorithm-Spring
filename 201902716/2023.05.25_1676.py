import math

def main():
    N = int(input())
    n_fac = math.factorial(N)
    zero = 0
    
    while n_fac % 10 == 0:
        zero += 1
        n_fac //= 10

    print(zero)
    
if __name__ == '__main__':
    main()

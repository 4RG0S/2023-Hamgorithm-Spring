def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print("yes")
    
    # A_factors = []
    # i = 2
    
    # while i <= A:
    #     if A % i == 0:
    #         A_factors.append(i)
    #         A = A // i
    #     else:
    #         i += 1
            
    # if sum(A_factors) == B:
    #     print("yes")
    # else:
    #     print("no")
          
if __name__ == '__main__':
    main()

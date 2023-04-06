if __name__ == "__main__":
    N = int(input())
    
    dp_arr = [0] * 11
    dp_arr[1] = 1
    dp_arr[2] = 2
    dp_arr[3] = 4
    
    for i in range(4, 11):
        dp_arr[i] = dp_arr[i - 1] + dp_arr[i - 2] + dp_arr[i - 3]
    
    for _ in range(N):
        test_num = int(input())
        print(dp_arr[test_num])
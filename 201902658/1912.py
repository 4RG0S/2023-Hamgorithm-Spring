if __name__ == "__main__":
    N = int(input())
    init_list = list(map(int, input().split()))
    
    sum_list = [init_list[0]]
    
    for i in range(len(init_list) - 1):
        sum_list.append(max(sum_list[i] + init_list[i + 1], init_list[i + 1]))
    
    print(max(sum_list))
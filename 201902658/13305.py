if __name__ == "__main__":
    K = int(input())
    distance = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    result = 0
    
    C = cost[0]
    for i in range(K - 1):
        if C > cost[i]:
            C = cost[i]
        result += C * distance[i]
    print(result)
if __name__ == "__main__":
    N = int(input())
    people = list(map(int, input().split()))
    
    people.sort()
    result = 0
    
    for i in range(1, N + 1):
        result += sum(people[0:i])
    print(result)
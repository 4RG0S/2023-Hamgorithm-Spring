if __name__ == "__main__":
    string = input().split("-")
    numbers = []
    
    for i in string:
        sum = 0
        temp = i.split("+")
        for j in temp:
            sum += int(j)
        numbers.appends(sum)
    
    N = numbers[0]
    for i in range(1, len(numbers)):
        N -= numbers[i]
    print(N)
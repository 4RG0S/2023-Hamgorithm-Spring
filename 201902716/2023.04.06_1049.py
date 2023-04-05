def c61(n, six, one):
    if six > (one * n):
        return (one * n)
    else:
        return six
    
def main():
    n, m = map(int, input().split())
    cost = 0
    six_list = []
    one_list = []
    for _ in range(m):
        a, b = map(int, input().split())
        six_list.append(a)
        one_list.append(b)
    
    six = min(six_list)
    one = min(one_list)
    
    if six > (one * 6):
        cost += (one * n)
    else:
        cost += (n // 6) * six  
        cost += c61(n % 6, six, one)

    print(cost)

if __name__ == '__main__':
    main()


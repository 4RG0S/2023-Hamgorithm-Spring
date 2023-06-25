def choidae_gongyaksu(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def choiso_gongbaesu(a, b):
    return a * b // choidae_gongyaksu(a, b)

def main():
    a, b = map(int, input().split())
    print(choidae_gongyaksu(a, b), choiso_gongbaesu(a, b))

if __name__ == '__main__':
    main()

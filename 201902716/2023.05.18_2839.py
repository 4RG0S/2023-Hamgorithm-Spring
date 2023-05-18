def main():
    N = int(input())
    bag5 = N // 5
    
    while bag5 >= 0:
        if (N - (bag5 * 5)) % 3 == 0:
            bag3 = (N - (bag5 * 5)) // 3
            print(bag5 + bag3)
            break
        bag5 -= 1
    else:
        print(-1)

if __name__ == '__main__':
    main()

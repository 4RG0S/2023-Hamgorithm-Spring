def main():
    n = int(input())
    n_list = list(str(n))
    n_list.sort(reverse=True)
    result = int(''.join(n_list))
    print(result)
    
if __name__ == '__main__':
    main()

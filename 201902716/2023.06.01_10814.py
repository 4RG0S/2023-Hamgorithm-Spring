def main():
    N = int(input())
    members = []
    
    for _ in range(N):
        age, name = map(str, input().split())
        members.append([int(age), name])
        
    members.sort(key=lambda x: x[0])
    
    for m in members:
        print(*m)

if __name__ == '__main__':
    main()

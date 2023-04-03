def main():
    n = int(input())
    room = []
    for _ in range(n):
        room.append(input())
        
    row_count = 0
    col_count = 0
    
    for i in range(n):
        empty_count = 0
        for j in range(n):
            if room[i][j] == ".":
                empty_count += 1
            else:
                if empty_count >= 2:
                    row_count += 1
                empty_count = 0
        if empty_count >= 2:
            row_count += 1
            
    for i in range(n):
        empty_count = 0
        for j in range(n):
            if room[j][i] == ".":
                empty_count += 1
            else:
                if empty_count >= 2:
                    col_count += 1
                empty_count = 0
        if empty_count >= 2:
            col_count += 1
    
    print(row_count, col_count)
    
if __name__ == '__main__':
    main()


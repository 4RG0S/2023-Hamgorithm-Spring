def colorChange(color):
    if color == 'B':
        color = 'W'
    else:
        color = 'B'
    return color
        
def findNum(i, j, chessboard, color):
    color_num = 0
    color_check = color
    for k in range(i, i+8):
        for l in range(j, j+8):
            if chessboard[k][l] != color_check:
                color_num += 1
            color_check = colorChange(color_check)
        color_check = colorChange(color_check)
                
    return color_num

def main():
    N, M = map(int, input().split())
    chessboard = [list(map(str, input())) for _ in range(N)]
    color_num_list = []

    for i in range(N-7):
        for j in range(M-7):
            color_num_list.append(findNum(i, j, chessboard, 'B'))
            color_num_list.append(findNum(i, j, chessboard, 'W'))
    
    print(min(color_num_list))
        
if __name__ == '__main__':
    main()

            

n = int(input())

row = col = 1

LEFT = True
RIGHT = False

direction = RIGHT

for _ in range(1, n):
    if direction == LEFT:
        if col == 1:
            row += 1
            direction = RIGHT
        else: row += 1; col -= 1
    else:
        if row == 1:
            col += 1
            direction = LEFT
        else: row -= 1; col += 1
print("%d/%d" %(row, col))

'''
zigzag 방향: row -1 , col + 1 방향 and row + 1, col -1 방향 존재,
1번 방향은 row가 1일 때 col만 + 1 하고 방향을 2로 바꿈
2번 방향은 col이 1일 때 row만 + 1 하고 방향을 1로 바꾼다.
'''
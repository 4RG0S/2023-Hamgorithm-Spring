import sys
input = sys.stdin.readline


row, col, inventory = map(int, input().split())
blocks = []
for i in range(row):
    blocks += list(map(int, input().split()))

min_time = 500*500*2*257
ans_height = blocks[0]
blocks_out = sum(blocks)
for target_h in range(max(blocks), min(blocks) - 1, -1):
    if blocks_out + inventory >= target_h * row * col:
        time = 0
        for b in blocks:
            diff = b - target_h
            if diff > 0:
                time += diff * 2
            elif diff < 0:
                time -= diff * 1

        if time < min_time:
            min_time = time
            ans_height = target_h

print(min_time, ans_height)
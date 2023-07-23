import sys
testcase = int(sys.stdin.readline())
for _ in range (testcase):
    bridge = int(sys.stdin.readline())
    start = 0
    mid = 0
    end = bridge+1
    #이진탐색 시작
    while start+1<end:
        mid = (start+end)//2 # 중앙값 저장 (mid값이 최대 밟는 징검다리 수가 됨)
        if (mid*(mid+1))//2 <= bridge: #등차수열의 합 공식 사용
            start = mid
        else: # 합이 다리수보다 커지면 앞쪽으로 구간을 줄여준다.
            end = mid
    print(start)

l = int(input())
s = input()
search = {}

def search_length(start, end, answer):
    if start > end:
        return answer
    mid = (start + end) // 2
    for i in range(l-mid+1):
        temp = s[i:i+mid]
        if search.get(temp):
            return search_length(mid+1, end, mid)
        else:
            search[temp] = True
    return search_length(start, mid-1, answer)

print(search_length(1, l, 0))

# 1. 이분탐색을 이용하여 길이를 찾는다. log n
# 2. 길이를 찾으면 그 길이를 기준으로 중복되는 문자열이 있는지 확인한다. n
# n * log n으로 시간 복잡도에서 통과할 수 있다.

# 메모리 관련 복잡도 역시 n이어야 한다. (n^2 일 경우 메모리 초과가 발생했다 ㅠㅠ)
# 괜히 플래문제가 아니다... 다음에 다시 도전함
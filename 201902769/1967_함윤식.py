import sys
sys.setrecursionlimit(10**6)
treeMap = {}
sum_list = [0]

def theSearch(a, distance):

    if len(treeMap[a]) != 0:
        childList = [0]
        for b, c in treeMap[a]:
            childList.append(theSearch(b, c))
        
        childList.sort()
        sum_list.append(childList[-1] + childList[-2])
        distance += childList[-1]

    return distance
        

n = int(input())

for i in range(1,n+1):
    treeMap[i] = []

for _ in range(n-1):
    a,b,c = map(int, input().split())
    treeMap[a].append([b,c])

theSearch(1, 0)
print(max(sum_list))
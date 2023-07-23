N, C = map(int,input().split())

location = []

for _ in range(N) :
    location.append(int(input()))

location.sort()

min_distance_per_location = (location[-1]-location[0]+1)//C
min_distance = 1000000000

answer = 0
count = 0
num = 0
for i in range(1,N) :

    if location[num]+min_distance_per_location <= location[i] :
        count += 1

        if location[i] - location[num] > answer and location[i] - location[num] <= min_distance:
            answer = location[i] - location[num]
            min_distance = location[i] - location[num]
        
        num = i

        if count == C :
            break

print(answer)

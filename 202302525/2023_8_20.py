import sys
input = sys.stdin.readline

# def caltime(arg):
#     hour, minute = arg.split(":")
#     hour = int(hour)
#     min = int(min)

#     return hour * 100 + minute

s, e, q = input().split()

table = {}
# start = caltime(s)
# end = caltime(e)
# q = caltime(q)
result = set()

while True:
    try:
        time, name = input().split()

        # time = caltime(time)
        if time <= s:
            table[name] = 1

        elif time >= e and time <= q:
            if name in table:
                result.add(name)
            
    except:
        break

print(len(result))
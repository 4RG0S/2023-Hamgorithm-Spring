List = []

for i in range(10):
    a = int(input())
    List.append(a%42)
List = set(List)
print(len(List))

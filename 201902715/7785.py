import sys

n = int(sys.stdin.readline())
record = {}
for _ in range(n):
    name, status = sys.stdin.readline().strip().split()
    if status == "enter":
        record[name] = status
    else:
        if name in record:
            del record[name]

print("\n".join(reversed(sorted(list(record.keys())))))
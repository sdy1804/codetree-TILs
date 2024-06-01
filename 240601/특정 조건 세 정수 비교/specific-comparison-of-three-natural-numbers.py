a, b, c = map(int, input().split())

lowest = min(a, b, c)

if a == lowest:
    print(1, end=" ")
else:
    print(0, end=" ")
if a == b and b == c and a == c:
    print(1, end=" ")
else:
    print(0, end=" ")
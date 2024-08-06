A, B, x, y = map(int, input().split())

dist = 0
if abs(A - x) < abs(A - y):
    dist = abs(A - x) + abs(B - y)
elif abs(A - y) < abs(A - x):
    dist = abs(A - y) + abs(B - x)

if dist > abs(A - B):
    print(abs(A - B))
else:
    print(dist)
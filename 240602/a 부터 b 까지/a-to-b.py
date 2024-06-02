a, b = map(int, input().split())

print(a, end=" ")
n = a
if n % 2 == 0:
    n += 3
else:
    n *= 2

for i in range(a, b+1):
    if n == i and n % 2 == 0:
        print(i, end= ' ')
        n += 3
    elif n == i and n % 2 != 0:
        print(i, end= ' ')
        n *= 2
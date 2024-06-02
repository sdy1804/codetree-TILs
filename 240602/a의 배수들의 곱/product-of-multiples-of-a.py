a, b = map(int, input().split())
prod = 1

for i in range(1, b):
    if i % a == 0:
        prod *= i
print(prod)
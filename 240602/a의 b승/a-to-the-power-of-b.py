a, b = map(int, input().split())
prod = 1

for i in range(b):
    prod *= a
print(prod)
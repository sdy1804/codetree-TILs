def squared(A, B):
    prod = 1
    for i in range(B):
        prod *= A
    return prod

a, b = map(int, input().split())
print(squared(a,b))
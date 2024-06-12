n, m = map(int, input().split())
A = list(map(int, input().split()))



def array_sums(a, b):
    sums = 0
    for i in range(a - 1, b):
        sums += A[i]
    return sums

for j in range(m):
    a1, a2 = map(int, input().split())
    print(array_sums(a1, a2))
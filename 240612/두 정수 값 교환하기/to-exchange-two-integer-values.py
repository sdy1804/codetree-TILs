def swap(A, B):
    A, B = B, A
    return A, B

n , m = map(int, input().split())
n, m = swap(n, m)
print(n, m)
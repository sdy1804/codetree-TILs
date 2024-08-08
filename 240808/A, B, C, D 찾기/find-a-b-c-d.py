arr = list(map(int, input().split()))

arr.sort()

A, B, C = arr[0], arr[1], arr[2]
D = arr[-1] - (A + B + C)
print(A, B, C, D)
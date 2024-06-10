A = input()
B = input()
n = 1

for i in range(len(A)):
    A = A[-1] + A[:-1]
    if n == len(A):
        print(-1)
    if A != B:
        n += 1
    else:
        print(n)
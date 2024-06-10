A = input()
B = input()

while B in A:
    i = A.index(B)
    A = A[:i] + A[i+len(B):]
print(A)
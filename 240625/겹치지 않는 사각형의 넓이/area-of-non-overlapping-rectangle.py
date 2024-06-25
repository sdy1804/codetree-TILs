A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = list(map(int, input().split()))

OFFSET = 0
for i in range(len(A)):
    if A[i] < OFFSET:
        OFFSET = A[i]

for i in range(len(B)):
    if B[i] < OFFSET:
        OFFSET = B[i]

for i in range(len(M)):
    if M[i] < OFFSET:
        OFFSET = M[i]

for i in range(len(A)):
        A[i] += abs(OFFSET)

for i in range(len(B)):
        B[i] += abs(OFFSET)

for i in range(len(M)):
        M[i] += abs(OFFSET)

ans = [[0] * 2100 for _ in range(2100)]

for i in range(A[0], A[2]):
    for j in range(A[1], A[3]):
        ans[i][j] = 1

for i in range(B[0], B[2]):
    for j in range(B[1], B[3]):
        ans[i][j] = 1

for i in range(M[0], M[2]):
    for j in range(M[1], M[3]):
        ans[i][j] = 2

count = 0
for i in range(len(ans)):
    count += ans[i].count(1)
print(count)
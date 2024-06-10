A = input()
B = input()
cnt = 0

for i in range(len(A) - 1):
    if A[i] == B[0] and A[i+1] == B[1]:
        cnt += 1
print(cnt)
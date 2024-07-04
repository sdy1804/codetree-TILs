n = int(input())
A = input()

cnt = 0
for i in range(len(A)):
    if A[i] == 'C':
        for j in range(i + 1, len(A)):
            if A[j] == 'O':
                for k in range(j + 1, len(A)):
                    if A[k] == 'W':
                        cnt += 1
print(cnt)
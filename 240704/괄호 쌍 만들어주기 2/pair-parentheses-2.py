A = input()

cnt = 0
for i in range(len(A)):
    if A[i] == '(' and A[i + 1] == '(':
        for j in range(i+2, len(A) - 1):
            if A[j] == ')' and A[j + 1] == ')':
                cnt += 1
print(cnt)
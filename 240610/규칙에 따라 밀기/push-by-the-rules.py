A = input()
command = list(input())
# print(A, command)

for comm in command:
    if comm == 'L':
        A = A[1:] + A[0]
    else:
        A = A[-1] + A[:-1]
print(A)
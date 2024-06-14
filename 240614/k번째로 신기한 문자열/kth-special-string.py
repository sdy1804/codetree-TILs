n, k, T = input().split()
n, k = int(n), int(k)
arr = [input() for _ in range(n)]

T_arr = []
# for i in range(n):
#     cnt = 0
#     for j in range(len(T)):
#         if arr[i][j] == T[j]:
#             cnt += 1
#     if cnt == len(T):
#         T_arr.append(arr[i])
for i in range(n):
    if len(arr[i]) >= len(T):
        if arr[i][:len(T)] == T:
            T_arr.append(arr[i])

T_arr.sort()
# print(T_arr)

print(T_arr[k-1])
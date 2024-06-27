N, M = map(int, input().split())
move_A = [list(map(int, input().split())) for _ in range(N)]
move_B = [list(map(int, input().split())) for _ in range(M)]

length_arr = 1000000
arr_A = [0] * length_arr
arr_B = [0] * length_arr

A_now_index = 1
for i in range(len(move_A)):
    for _ in range(move_A[i][1]):
        arr_A[A_now_index] = arr_A[A_now_index - 1] + move_A[i][0]
        A_now_index += 1
for i in range(len(arr_A)):
    if i >= A_now_index:
        arr_A[i] = arr_A[A_now_index-1]
# print(arr_A)

B_now_index = 1
for i in range(len(move_B)):
    for _ in range(move_B[i][1]):
        arr_B[B_now_index] = arr_B[B_now_index - 1] + move_B[i][0]
        B_now_index += 1
for i in range(len(arr_B)):
    if i >= B_now_index:
        arr_B[i] = arr_B[B_now_index-1]
# print(arr_B)

case = 0
for i in range(1, len(arr_A)):
    if arr_A[i] > arr_B[i] and arr_A[i-1] <= arr_B[i-1]:
        case += 1
    elif arr_A[i] < arr_B[i] and arr_A[i-1] >= arr_B[i-1]:
        case += 1
    elif arr_A[i] == arr_B[i] and (arr_A[i-1] < arr_B[i-1] or arr_A[i-1] > arr_B[i-1]):
        case += 1
print(case)
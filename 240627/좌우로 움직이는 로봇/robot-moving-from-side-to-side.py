n, m = map(int, input().split())
move_A = [list(input().split()) for _ in range(n)]
move_B = [list(input().split()) for _ in range(m)]

for i in range(len(move_A)):
    move_A[i][0] = int(move_A[i][0])
for i in range(len(move_B)):
    move_B[i][0] = int(move_B[i][0])

length_arr = 1000000
arr_A = [0] * length_arr
arr_B = [0] * length_arr

A_now_index = 1
for i in range(len(move_A)):
    if move_A[i][1] == 'L':
        for j in range(move_A[i][0]):
            arr_A[A_now_index] = arr_A[A_now_index - 1] - 1
            A_now_index += 1
    elif move_A[i][1] == 'R':
        for j in range(move_A[i][0]):
            arr_A[A_now_index] = arr_A[A_now_index - 1] + 1
            A_now_index += 1
for i in range(len(arr_A)):
    if i >= A_now_index:
        arr_A[i] = arr_A[A_now_index - 1]
# print(arr_A)

B_now_index = 1
for i in range(len(move_B)):
    if move_B[i][1] == 'L':
        for j in range(move_B[i][0]):
            arr_B[B_now_index] = arr_B[B_now_index - 1] - 1
            B_now_index += 1
    elif move_B[i][1] == 'R':
        for j in range(move_B[i][0]):
            arr_B[B_now_index] = arr_B[B_now_index - 1] + 1
            B_now_index += 1
for i in range(len(arr_B)):
    if i >= B_now_index:
        arr_B[i] = arr_B[B_now_index - 1]
# print(arr_B)

meet_count = 0
for i in range(1, len(arr_A)):
    if arr_A[i] == arr_B[i] and arr_A[i-1] != arr_B[i-1]:
        meet_count += 1
print(meet_count)
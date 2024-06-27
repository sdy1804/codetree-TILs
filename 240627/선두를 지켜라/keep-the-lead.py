N, M = map(int, input().split())
move_A = [list(map(int, input().split())) for _ in range(N)]
move_B = [list(map(int, input().split())) for _ in range(M)]

length_arr = 1000000
arr_A = [0] * length_arr
arr_B = [0] * length_arr

A_now_index = 1
for i in range(len(move_A)):
    for j in range(move_A[i][1]):
        arr_A[A_now_index] = arr_A[A_now_index - 1] + move_A[i][0]
        A_now_index += 1
# print(arr_A)

B_now_index = 1
for i in range(len(move_B)):
    for j in range(move_B[i][1]):
        arr_B[B_now_index] = arr_B[B_now_index - 1] + move_B[i][0]
        B_now_index += 1
# print(arr_B)

start_index = 0
A_first = None
for i in range(len(arr_A)):
    if arr_A[i] > arr_B[i]:
        A_first =True
        start_index = i
        break
    elif arr_A[i] < arr_B[i]:
        A_first = False
        start_index = i
        break

count_change = 0
for i in range(start_index + 1, len(arr_A)):
    if A_first == True and arr_A[i] < arr_B[i]:
        A_first = False
        count_change += 1
    elif A_first == False and arr_A[i] > arr_B[i]:
        A_first = True
        count_change += 1
print(count_change)
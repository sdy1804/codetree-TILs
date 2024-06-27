N, M = map(int, input().split())
move_A = [list(input().split()) for _ in range(N)]
move_B = [list(input().split()) for _ in range(M)]

for i in range(len(move_A)):
    move_A[i][1] = int(move_A[i][1])
for i in range(len(move_B)):
    move_B[i][1] = int(move_B[i][1])

# 입력된 명령어들을 수행하는 동안
# 배열의 인덱스는 계속 증가하되 R이면 이전 값에서 1씩 증가, L이면 이전 값에서 1씩 감소

length_arr = 2100
arr_A = [0] * length_arr
arr_B = [0] * length_arr
A_now_index = 1
B_now_index = 1

for i in range(len(move_A)):
    if move_A[i][0] == 'R':
        for j in range(move_A[i][1]):
            arr_A[A_now_index] = arr_A[A_now_index - 1] + 1
            A_now_index += 1
    elif move_A[i][0] == 'L':
        for k in range(move_A[i][1]):
            arr_A[A_now_index] = arr_A[A_now_index - 1] - 1
            A_now_index += 1
# print(arr_A)

for i in range(len(move_B)):
    if move_B[i][0] == 'R':
        for j in range(move_B[i][1]):
            arr_B[B_now_index] = arr_B[B_now_index - 1] + 1
            B_now_index += 1
    elif move_B[i][0] == 'L':
        for k in range(move_B[i][1]):
            arr_B[B_now_index] = arr_B[B_now_index - 1] - 1
            B_now_index += 1
# print(arr_B)

no_match = True
for i in range(len(arr_A)):
    if arr_A[i] != 0 and arr_A[i] == arr_B[i]:
        print(i)
        no_match = False
        break
if no_match:
    print(-1)
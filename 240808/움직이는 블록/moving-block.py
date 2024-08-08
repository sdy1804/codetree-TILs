N = int(input())
arr = [int(input()) for _ in range(N)]

# 제일 큰 값을 빼야 함
# 모든 수를 더해서 N으로 나눈 값이 동일해지는 값 -> 최종 블록 갯수
# Q1. 얼마나 뺄 것인가? -> 2번째로 큰 수를 기준으로 빼야 할듯
# Q2. 뺀 값을 어디에 옮길 것인가? -> 모든 수에 더해봐서 최종 블록 갯수와 차이가 적은 곳에 놓기

ans_block_num = sum(arr) // N
ans_arr = [ans_block_num] * N
cnt_block = 0

while arr != ans_arr:
    max_val = max(arr)
    second_max_val = 0

    for i in range(len(arr)):
        if max_val == arr[i]:
            max_val_idx = i

    for j in range(len(arr)):
        if j != max_val_idx and arr[j] < max_val:
            second_max_val = max(second_max_val, arr[j])
    # print('max_val, second_max_val', max_val, second_max_val)
    
    diff = max_val - second_max_val
    cnt_block += diff
    temp_arr = arr.copy()
    min_diff = 100000
    for k in range(len(arr)):
        if temp_arr[k] != ans_block_num:
            temp_arr[k] += diff
    for k in range(len(arr)):
        if arr[k] != ans_block_num:
            now_diff = abs(temp_arr[k] - ans_block_num)
            min_diff = min(now_diff, min_diff)
            if min_diff == now_diff:
                now_min_diff_idx = k
    arr[now_min_diff_idx] += diff
    arr[max_val_idx] -= diff
    # print(arr)
print(cnt_block)
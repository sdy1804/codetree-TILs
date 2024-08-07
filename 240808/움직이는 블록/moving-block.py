N = int(input())
arr = [int(input()) for _ in range(N)]

# 제일 큰 값을 빼야 함
# 모든 수를 더해서 N으로 나눈 값이 동일해지는 값 -> 최종 블록 갯수
# Q1. 얼마나 뺄 것인가? -> 2번째로 큰 수를 기준으로 빼야 할듯
# Q2. 뺀 값을 어디에 옮길 것인가? -> 모든 수에 더해봐서 최종 블록 갯수와 차이가 적은 곳에 놓기

ans_block_num = sum(arr) // N
ans_arr = [ans_block_num] * N
cnt_block = 0

for blocks in arr:
    if blocks > ans_block_num:
        cnt_block += blocks - ans_block_num
print(cnt_block)
N = int(input())
arr = [int(input()) for _ in range(N)]

# 완탐의 범위는 0부터 최대 빙산 높이까지로 설정 가능
# 살아남은 빙산 체크법 -> 설정된 물높이에서 모두 뺏을 때 0보다 큰 수들
# block수가 증가할 조건 : 인덱스가 0인데 0보다 큰값일 때 / 현재 0보다 큰 값이고 이전 값이 0보다 작거나 같은 값일 때
# block수가 유지될 조건 : 현재 값이 0보다 작을 때 / 현재 값이 0보다 큰 값인데 왼쪽 값이 0보다 큰 값일 때
block_max = 0
for i in range(max(arr) + 1):
    arr2 = arr.copy()
    # print(i)
    now_block = 0
    for j in range(len(arr2)):
        arr2[j] = arr2[j] - i
    for k in range(len(arr2)):
        if (k == 0 and arr2[k] > 0) or (arr2[k] > 0 and arr2[k-1] <= 0):
            now_block += 1
        if (arr2[k] < 0) or (arr2[k] > 0 and arr2[k-1] > 0):
            now_block = now_block
    block_max = max(now_block, block_max)
    # print(now_block)
    # print(arr2)
print(block_max)
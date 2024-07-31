N, L = map(int, input().split())
arr = list(map(int, input().split()))
# arr.sort()
# print(arr)
# 앞 유형과 마찬가지로 최댓값 설정
# 최댓값이 0 일 때 -> 1을 L개 더해서 0보다 큰수를 0개 이상 만들 수 있으면 최댓값 만족
# 최댓값이 1 일 때 -> 1을 L개 더해서 1보다 큰수가 1개 이상 만들 수 있으면 최댓값 만족
# 최댓값이 2 일 때 -> 1을 L개 더해서 2보다 큰수가 2개 이상 만들 수 있으면 최댓값 만족
# 최댓값이 3 일 때 -> 3보다 작은 값들에 1을 더해서 만족하면 최댓값 만족

# 만약 1 증가시킬 수 있는 횟수가 여러번일 때는?? -> 어차피 1개 증가까지만 의미가 있는 듯 함
# 1 증가 이기 때문에 연속된 숫자에서 의미가 있음

total_max = 0
for i in range(max(arr)+1):
    now_cnt = 0
    if L == 0:
        for j in range(len(arr)):
            if arr[j] >= i:
                now_cnt += 1
    if now_cnt >= i:
        total_max = max(total_max, i)
    # print(total_max)
    if L > 0:
        max_idx = 0
        plus = L
        for j in range(len(arr)):
            if arr[j] < i:
                max_idx = max(j, max_idx)
        for j in range(len(arr)):
            if arr[j] == arr[max_idx]:
                arr[j] += 1
        # arr[max_idx] += 1
        for k in range(len(arr)):
            if arr[k] >= i:
                now_cnt += 1
        arr[max_idx] -= 1
    if now_cnt >= i:
        total_max = max(total_max, i)
print(total_max)
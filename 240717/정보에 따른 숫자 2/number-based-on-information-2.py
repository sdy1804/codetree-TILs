import sys

T, a, b = map(int, input().split())
arr = [list(input().split()) for _ in range(T)]
for i in range(len(arr)):
    arr[i][1] = int(arr[i][1])

# a부터 b까지 완탐
# arr를 탐색 - S이면서 현재와 차이값이 가장 작은 s을 저장
# 마찬가지로 N이면서 현재와 차이값이 가장 작은 n을 저장
# s <= n을 만족하면 cnt 증가
cnt = 0
for i in range(a, b+1):
    s, n = 0, 0
    max_min_s, max_min_n = sys.maxsize, sys.maxsize
    for j in range(len(arr)):
        now_min_s, now_min_n = 0, 0
        if arr[j][0] == 'S':
            now_min_s = abs(arr[j][1] - i)
            max_min_s = min(now_min_s, max_min_s)
        if arr[j][0] == 'N':
            now_min_n = abs(arr[j][1] - i)
            max_min_n = min(now_min_n, max_min_n)
    # print('s, n',max_min_s, max_min_n)
    if max_min_s <= max_min_n:
        cnt += 1
print(cnt)
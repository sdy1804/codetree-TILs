n, m = map(int, input().split())
arr = list(map(int, input().split()))

total_max = 0
for i in range(len(arr)): # 시작위치
    now_point = i
    source = 0
    for j in range(m):
        # print('arr[now_point]', arr[now_point])
        source += arr[now_point]
        # print('source', source)
        now_point = arr[now_point] - 1
        # print('now_point', now_point)
    total_max = max(source, total_max)
print(total_max)
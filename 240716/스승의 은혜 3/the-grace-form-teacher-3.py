N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = arr.copy()
arr.sort(key=lambda x: (x[0] + x[1]))
arr2.sort(key=lambda x: (x[0] // 2 + x[1]))
# print(arr)

total_cnt = 0
for i in range(len(arr)):
    total_sum = 0
    now_cnt = 0
    for j in range(len(arr)):
        if i == j:
            arr[j][0] = arr[j][0] // 2
        # print(arr[j])
        total_sum += sum(arr[j])
        # print('total_sum', total_sum)
        if total_sum <= B:
            now_cnt += 1
            # print('cnt', now_cnt)
        total_cnt = max(now_cnt, total_cnt)
        # print('total_cnt', total_cnt)
        if i == j:
            arr[j][0] = arr[j][0] * 2
# print(total_cnt)

total_cnt2 = 0
for i in range(len(arr2)):
    total_sum2 = 0
    now_cnt2 = 0
    for j in range(len(arr2)):
        if i == j:
            arr2[j][0] = arr2[j][0] // 2
        # print(arr[j])
        total_sum2 += sum(arr2[j])
        # print('total_sum', total_sum)
        if total_sum2 <= B:
            now_cnt2 += 1
            # print('cnt', now_cnt)
        total_cnt2 = max(now_cnt2, total_cnt2)
        # print('total_cnt', total_cnt)
        if i == j:
            arr2[j][0] = arr2[j][0] * 2
# print(total_cnt2)
print(max(total_cnt2, total_cnt))
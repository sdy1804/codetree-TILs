N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = arr.copy()
arr3 = arr.copy()
arr.sort(key=lambda x: (x[0] + x[1]))
# print(arr)
arr2.sort(key=lambda x: (x[0] // 2 + x[1]))
# print(arr2)
arr3.sort(key=lambda x: (x[0] + x[1], x[0] // 2 + x[1]))
# print(arr3)
# print(arr)

total_cnt = 0
for i in range(len(arr)):
    total_sum = 0
    now_cnt = 0
    for j in range(len(arr)):
        if i == j:
            arr[j][0] = arr[j][0] // 2
        # print(arr[j], sum(arr[j]), arr[j][0] // 2 + arr[j][1])
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

total_cnt3 = 0
for i in range(len(arr3)):
    total_sum3 = 0
    now_cnt3 = 0
    for j in range(len(arr3)):
        # print(arr[j])
        total_sum3 += sum(arr3[j])
        # print('total_sum', total_sum)
        if total_sum3 <= B:
            now_cnt3 += 1
        else:
            total_sum3 -= sum(arr3[j])
            for k in range(j, len(arr3)):
                # print(arr3[k], total_sum3)
                # print(arr3[k][0] // 2 + arr3[k][1] + total_sum3)
                if (arr3[k][0] // 2 + arr3[k][1]) + total_sum3 <= B:
                    now_cnt3 += 1
                    total_sum3 += arr3[k][0] // 2 + arr3[k][1]
        total_cnt3 = max(now_cnt3, total_cnt3)
        # print('total_cnt', total_cnt)
        if i == j:
            arr3[j][0] = arr3[j][0] * 2
# print(total_cnt3)
print(max(total_cnt, total_cnt2, total_cnt3))
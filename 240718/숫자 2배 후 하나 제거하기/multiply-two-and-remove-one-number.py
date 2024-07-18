import sys

n = int(input())
arr = list(map(int, input().split()))

total_min = sys.maxsize
for i in range(n):
    arr[i] = arr[i] * 2
    for j in range(n):
        remain_arr = []
        for k, elem in enumerate(arr):
            if j != k:
                remain_arr.append(elem)
        # print('remain_arr', remain_arr)
        now_sum = 0
        for l in range(len(remain_arr) - 1):
            # print('arr[l], arr[l+1]', remain_arr[l], remain_arr[l+1])
            now_sum += abs(remain_arr[l] - remain_arr[l+1])
        # print(now_sum)
        total_min = min(now_sum, total_min)
        # print(total_min)
    arr[i] = arr[i] // 2
print(total_min)
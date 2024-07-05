N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    now_sum = 0
    now_list = []
    nums = 0
    for j in range(i, N):
        nums += 1
        now_sum += arr[j]
        # print('nums', nums)
        # print('now_sum', now_sum)
        now_list.append(arr[j])
        # print(now_list)
        avg = now_sum / nums
        # print('i, j',i, j)
        # print('avg', avg)
        if avg in now_list:
            cnt += 1
            # print(cnt)
print(cnt)
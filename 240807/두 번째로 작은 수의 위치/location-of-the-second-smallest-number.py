n = int(input())
arr = list(map(int, input().split()))

# 1. 제일 작은 수를 찾음
# 2. 제일 작은 수보다 크지만, 그중에 가장 작은 수를 찾음.
# 3. 두번째로 작은 수를 count.
# 4. count가 1이면 해당 수의 인덱스를 +1 하여 출력, 그 외의 수는 -1 출력

least_num = 10000
for idx in range(n):
    least_num = min(least_num, arr[idx])

second_least_num = 1000
second_idx = 0
for i in range(n):
    if arr[i] > least_num:
        second_least_num = min(second_least_num, arr[i])
        if second_least_num == arr[i]:
            second_idx = i
# print('second_least_num', second_least_num)
# print('second_idx', second_idx)

cnt = arr.count(second_least_num)
# print('second_num cnt', cnt)

if cnt == 1:
    print(second_idx+1)
else:
    print(-1)
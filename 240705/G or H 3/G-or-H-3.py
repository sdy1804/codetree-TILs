N, K = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]
for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])
length = 21
new_arr = [0] * length
for i in range(len(arr)):
    new_arr[arr[i][0]] = arr[i][1] 

total_max = 0
for i in range(1, len(new_arr)-K):
    now_points = 0
    for j in range(i, i+K+1):
        # print(j, new_arr[j])
        if new_arr[j] == 'G':
            now_points += 1
        elif new_arr[j] == 'H':
            now_points += 2
        # print(now_points)
    total_max = max(total_max, now_points)
print(total_max)
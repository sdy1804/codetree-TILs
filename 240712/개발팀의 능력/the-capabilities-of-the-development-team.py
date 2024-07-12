import sys

arr = list(map(int, input().split()))

def diff(a, b, c):
    val_max = max(a, b, c)
    val_min = min(a, b, c)
    return val_max - val_min

total_min = sys.maxsize
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        # print('i, j', arr[i],arr[j])
        first_sum = 0
        first_sum += arr[i] + arr[j]
        for k in range(len(arr)):
            for l in range(len(arr)):
                same_sum = False
                if k == i or k == j or l == i or l == j or k == l:
                    continue
                # print('k, l', arr[k], arr[l])
                second_sum = 0
                second_sum += arr[k] + arr[l]
                last_sum = sum(arr) - first_sum - second_sum
                # print('f, s, l', first_sum, second_sum, last_sum)
                if first_sum == second_sum or first_sum == last_sum or second_sum == last_sum:
                    same_sum = True
                    continue
                now_min = 0
                now_min = diff(first_sum, second_sum, last_sum)
                total_min = min(total_min, now_min)

if same_sum:
    print(-1)
else:
    print(total_min)
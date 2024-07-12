import sys

arr = list(map(int, input().split()))

def find_mindiff(a, b, c):
    val_max = max(a, b, c)
    val_min = min(a, b, c)
    return val_max - val_min

total_min = sys.maxsize
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        first_sum = 0
        # print('i, j', arr[i], arr[j])
        first_sum += arr[i] + arr[j]
        for k in range(len(arr)):
            for l in range(len(arr)):
                second_sum = 0
                now_min = 0
                if k == i or k == j or l == i or l == j or k == l:
                    continue
                # print('k, l', arr[k], arr[l])
                second_sum += arr[k] + arr[l]
                last_sum = sum(arr) - first_sum - second_sum
                # print('f, s, l', first_sum, second_sum, last_sum)
                now_min = find_mindiff(first_sum, second_sum, last_sum)
                # print(now_min)
                total_min = min(total_min, now_min)
print(total_min)

# 어떻게 3팀으로 쪼개서 합을 구할 것인가?
# 일단 완탐으로 처음 2명은 고를 수 있다
# 완탐을 2번 더 안에서 돌리는 방법?
# 만약 안에서 2번 더 도는 과정에서 앞선 i j가 나온다면 continue 그렇지 않다면 선택해서 합을 구하는 방식 시도
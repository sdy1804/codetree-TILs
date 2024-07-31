n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 최댓값을 어떻게 만들어 나갈 것인가??
# 예를 들어 최댓값 8일 때, 어떻게 8을 만드는 구간을 찾아서 자를 것인가??
# -> 딱 8을 만들어내는 것이 아닌, 최대값의 기준으로 그 이상 커지지 않도록 앞에서부터 만들기

for val_max in range(max(arr), sum(arr)+1):
    parts = arr[0]
    temp_sum = []
    for i in range(1, n):
        if parts + arr[i] > val_max:
            temp_sum.append(parts)
            parts = arr[i]
        else:
            parts += arr[i]
    temp_sum.append(parts)
    # print(temp_sum)
    if len(temp_sum) <= m:
        # print(len(temp_sum))
        print(val_max)
        break
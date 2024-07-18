N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 종이컵이 3개이므로 첫번째, 두번째, 세번째에 조약돌이 있을 경우로 완탐

max_cnt = 0
for i in range(3):
    # print('i',i)
    now_list = [0] * 3
    now_list[i] = 1
    cnt = 0
    for j in range(len(arr)):
        change_1 = arr[j][0] - 1
        change_2 = arr[j][1] - 1
        check_cup = arr[j][2] - 1
        now_list[change_1], now_list[change_2] = now_list[change_2], now_list[change_1]
        # print(now_list)
        if now_list[check_cup] == 1:
            cnt += 1
    max_cnt = max(cnt, max_cnt)
print(max_cnt)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 경우의 수
# 1 : 가위 2 : 바위 3 : 보  -> 1 > 3 > 2
# 1 : 가위 2 : 보 3 :바위 -> 1 > 2 > 3
# 1 : 바위 2 : 가위 3 : 보 -> 1 > 2 > 3
# 1 : 바위 2 : 보 3 : 가위 -> 1 > 3 > 2
# 1 : 보 2 : 바위 3 : 가위 -> 1 > 2 > 3
# 1 : 보 2 : 가위 3: 바위 -> 1 > 3 > 2
# 1 > 3 > 2 or 1 > 2 > 3

max_win = 0
win_cnt1 = 0
for i in range(len(arr)):
    if (arr[i][0] == 1 and arr[i][1] == 2) or (arr[i][0] == 2 and arr[i][1] == 3) or (arr[i][0] == 3 and arr[i][1] == 1):
        win_cnt1 += 1
# print(win_cnt1)

win_cnt2 = 0
for i in range(len(arr)):
    if (arr[i][0] == 1 and arr[i][1] == 3) or (arr[i][0] == 3 and arr[i][1] == 2) or (arr[i][0] == 2 and arr[i][1] == 1):
        win_cnt2 += 1
# print(win_cnt2)

max_win = max(win_cnt1, win_cnt2)
print(max_win)
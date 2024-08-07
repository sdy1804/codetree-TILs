n = int(input())
arr = [list(input().split()) for _ in range(n)]


# 현재 점수에 따라 이전 명당과 현재 명당이 다를 경우 카운트 증가

A_score, B_score = 0, 0
bef_hall_of_fame, now_hall_of_fame = ['A', 'B'], ['A', 'B']
cnt = 0

for idx in range(n):
    # print('bef_hall_of_fame', bef_hall_of_fame)
    if arr[idx][0] == 'A':
        A_score += int(arr[idx][1])
    elif arr[idx][0] == 'B':
        B_score += int(arr[idx][1])
    # print(A_score, B_score)
    if A_score > B_score:
        now_hall_of_fame = ['A']
    elif A_score < B_score:
        now_hall_of_fame = ['B']
    else:
        now_hall_of_fame = ['A', 'B']
    # print('now_hall_of_fame', now_hall_of_fame)
    if bef_hall_of_fame != now_hall_of_fame:
        cnt += 1
    bef_hall_of_fame = now_hall_of_fame
print(cnt)
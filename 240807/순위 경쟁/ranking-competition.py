n = int(input())
arr = [list(input().split()) for _ in range(n)]

# 이전 명당, 현재 명당 생성
# 각 스코어 계산
# 스코어에 따른 명당 변경
# 변경 될때마다 카운트 + 1

bef_hall_of_fame, now_hall_of_fame = ['A', 'B', 'C'], ['A', 'B', 'C']
A_score, B_score, C_score = 0, 0, 0
cnt = 0

for i in range(n):
    if arr[i][0] == 'A':
        A_score += int(arr[i][1])
    elif arr[i][0] == 'B':
        B_score += int(arr[i][1])
    elif arr[i][0] == 'C':
        C_score += int(arr[i][1])
    # print('A_score, B_score, C_score', A_score, B_score, C_score)

    if A_score == B_score == C_score:
        now_hall_of_fame = ['A', 'B', 'C']
    elif A_score == B_score > C_score:
        now_hall_of_fame = ['A', 'B']
    elif A_score == C_score > B_score:
        now_hall_of_fame = ['A', 'C']
    elif B_score == C_score > A_score:
        now_hall_of_fame = ['B', 'C']
    elif A_score > B_score and A_score > C_score:
        now_hall_of_fame = ['A']
    elif B_score > A_score and B_score > C_score:
        now_hall_of_fame = ['B']
    elif C_score > B_score and C_score > A_score:
        now_hall_of_fame = ['C']
    if bef_hall_of_fame != now_hall_of_fame:
        cnt += 1
    bef_hall_of_fame = now_hall_of_fame
    # print(now_hall_of_fame)
print(cnt)
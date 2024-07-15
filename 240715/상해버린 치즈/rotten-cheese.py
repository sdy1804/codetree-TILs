N, M, D, S = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(D)]
arr2 = [list(map(int, input().split())) for _ in range(S)]

# 예제 4번 치즈) 정확히 하나의 치즈만 상했을 것이니, arr2에 있는 사람들이 공통으로 먹은 치즈로 줄일 수 있음
# arr2 안에서 arr1을 돌리면서, 조건에 해당하며 범위안에 있는 치즈들 체크(상한 치즈 리스트)
# ex) 1번사람 돌렸을 때 -> 1, 2, 4번 치즈 후보(1) , 3번은 제외(0)
# 2번 사람 돌렸을 때 -> 1, 2번 치즈 후보(1), 3, 4번은 제외(0)
# 돌리고나서, arr1를 한번 돌리면서 상한 치즈 리스트에 있는 치즈를 먹은 사람 수를 모두 체크
# -> 약을 먹어야 하는 사람의 수를 구함

cheese_lst = [0] * (M + 1) # 상한 치즈 리스트

cnt = 0
for i in range(len(arr2)):
    now_cheese_lst = [0] * (M + 1)
    for j in range(len(arr1)):
        if arr1[j][0] == arr2[i][0] and arr1[j][2] < arr2[i][1]: # 조건에 있으면 상한 치즈로 체크
            now_cheese_lst[arr1[j][1]] = 1 # 몇번째 치즈가 상한 치즈인지 체크 # 현재 문제점 : 아픈 사람들이 모두 먹은 치즈인지 체크하지 않음
        # print(arr1[j], now_cheese_lst)
        if cnt == 0:
            cheese_lst = now_cheese_lst
    for k in range(len(cheese_lst)):
        # print('now, old', now_cheese_lst[k], cheese_lst[k])
        if cheese_lst[k] == now_cheese_lst[k]:
            cheese_lst[k] = cheese_lst[k]
        elif cheese_lst[k] != now_cheese_lst[k]:
            cheese_lst[k] = 0
    cnt += 1
    # print(cheese_lst)

total_max = 0
for i in range(1, M + 1):
    ans = [0] * (N + 1)
    for j in range(len(arr1)):
        if cheese_lst[i] == 1 and i == arr1[j][1] : # 상한 치즈의 인덱스와 현재 상한 치즈를 먹은 사람의 인덱스가 같을 때
            # print(arr1[j])
            ans[arr1[j][0]] = 1 # 약을 먹어야 하는 사람으로 체크
    now_max = ans.count(1)
    total_max = max(total_max, now_max)
print(total_max)
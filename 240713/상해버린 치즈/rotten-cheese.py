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

for i in range(len(arr2)):
    check_list = [k for k in range(1, M+1)]
    for j in range(len(arr1)):
        if arr1[j][0] == arr2[i][0] and arr1[j][2] < arr2[i][1]: # 조건에 있으면 상한 치즈로 체크
            cheese_lst[arr1[j][1]] = 1
        if arr1[j][0] == arr2[i][0]:
            if arr1[j][1] in check_list:
                check_list.remove(arr1[j][1]) # 제외시킬 치즈 인덱스들
    for k in check_list:
        cheese_lst[k] = 0
# print(cheese_lst)

ans = [0] * (N + 1)

for i in range(len(arr1)):
    for j in range(len(cheese_lst)):
        # print(i, j)
        if cheese_lst[j] == 1 and j == arr1[i][1]:
            # print(arr1[i])
            ans[arr1[i][0]] = 1
# print(ans)
print(ans.count(1))
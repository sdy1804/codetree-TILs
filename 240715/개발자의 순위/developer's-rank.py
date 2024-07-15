K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(K)]

# 첫번째 경기에서 순서쌍 만들기
# 두번째 경기부터 완탐을 통해 첫번째 경기 순서쌍 없을 경우 

test = []
total_line = []
cnt = 0
for i in range(K):
    now_line = []
    for j in range(len(arr[i])):
        for k in range(j + 1, len(arr[i])):
            # print(arr[i][j], arr[i][k])
            if cnt == 0:
                test.append([arr[i][j], arr[i][k]])
                total_line.append([arr[i][j], arr[i][k]])
            else:
                now_line.append([arr[i][j], arr[i][k]])
    if cnt != 0:
        for l in range(len(test)):
            if test[l] not in now_line:
                # print(test[l])
                if test[l] in total_line:
                    total_line.remove(test[l])
    # print('test',test)
    # print('now',now_line)
    # print(total_line)
    cnt += 1
print(len(total_line))
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

check_list = [[] for _ in range(11)]

for i in range(len(arr)):
    bird_num = arr[i][0]
    bird_line = arr[i][1]
    check_list[bird_num].append(bird_line)
# print(check_list)
cnt = 0
for j in range(len(check_list)):
    if check_list[j] == []:
        continue
    if check_list[j].count(1) == check_list[j].count(0):
        for k in range(len(check_list[j])-1):
            if check_list[j][k] != check_list[j][k+1]:
                cnt += 1
    elif check_list[j].count(1) != check_list[j].count(0):
        if check_list[j].count(1) == 0 or check_list[j].count(0) == 0:
            continue
        for k in range(len(check_list[j])-1):
            if check_list[j][k] != check_list[j][k+1]:
                cnt += 1
print(cnt)
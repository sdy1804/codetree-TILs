N = int(input())
arr = [list(input().split()) for _ in range(N)]
for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])

length = 101
people_list = [0] * length
for i in range(len(arr)):
    people_list[arr[i][0]] = arr[i][1]
# print(people_list)

# 처음부터 끝까지 하나씩 완.탐하면서 알파벳을 찾으면
# 찾은 지점부터 다음 알파벳이 나올 때,
# -> 알파벳 수가 G만 또는 H만 있을 때 max값 갱신
# -> 또는 G랑 H 값이 같을 때 max값 갱신
# -> 0일 때는 그냥 pass
# -> 카운트 수가 1일 때는 0

total_max = 0
for i in range(len(people_list)):
    now_max = 0
    if people_list[i] == 0:
        continue
    if people_list[i] == 'G' or people_list[i] == 'H':
        for j in range(i + 1, len(people_list)):
            if people_list[j] == 0:
                continue
            if people_list[i:j+1].count('G') == people_list[i:j+1].count('H') \
            or people_list[i:j+1].count('G') != 0 and people_list[i:j+1].count('H') == 0 \
            or people_list[i:j+1].count('G') == 0 and people_list[i:j+1].count('H') != 0: 
                now_max = j - i
                # print(now_max)
                total_max = max(total_max, now_max)
print(total_max)
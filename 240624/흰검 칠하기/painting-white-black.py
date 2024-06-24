n = int(input())
arr = list(input().split() for _ in range(n))
for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])

# 칠할 때마다 count 세기 -> 해당 인덱스와 동일한 list 생성
# 블랙이면 1, 화이트면 2로 값 변경
# 아무 것도 안 칠했으면 0
# 끝나고 나서 count의 인덱스가 4 라면, ans의 같은 인덱스의 값을 회색인 3으로 변경

count = [0] * 100 * 1000 * 2
ans = [0] * 100 * 1000 * 2
color = [''] * 10 * 100 * 1000 * 2
# color = [''] * 15
# count = [0] * 15
# ans = [0] * 15

start_point = 100000
# start_point = 5
for i in range(len(arr)):
    if arr[i][1] == 'R':
        for j in range(start_point, start_point + arr[i][0]):
            ans[j] = 1
            count[j] += 1
            color[j]+='B'
        start_point += arr[i][0] - 1
        # print(count)
    else:
        for j in range(start_point, start_point - arr[i][0], -1):
            ans[j] = 2
            count[j] += 1
            color[j]+='W'
        start_point = start_point - arr[i][0] + 1
        # print('white',count)

for i in range(len(count)):
    if count[i] >= 4 and color[i].count('B') >= 2 and color[i].count('W') >= 2:
        ans[i] = 3
# print(ans)
print(ans.count(2), ans.count(1), ans.count(3))
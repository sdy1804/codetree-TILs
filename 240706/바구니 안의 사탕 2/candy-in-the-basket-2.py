N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 리스트 만들고 위치에 해당하는 사탕 갯수 추가
# 구간 설정하여 완전 탐색
# 0 ~ 15까지 만들었을 때, K = 3
# c가 0일 경우 -> -3, 3
# c가 3일 경우 -> 0, 6
# c = 4 -> 1, 7
# c = 10 -> 7, 13
# c = 12 -> 9, 15
# c = 13 -> 10, 16

# 0~100까지 만들었을 때, K = 72
# c = 0 -> -72, 72
# c = 100-72 = 28 -> 
# c = 72 -> 0, 72+72=144
# out of range가 되는 경우 유의
length = 10000
candy_list = [0] * length
for i in range(len(arr)):
    candy_list[arr[i][1]] += arr[i][0]
# print(candy_list)

total_max = 0
for i in range(K, len(candy_list) - K): # 
    # print(i)
    # print('new')
    now_max = 0
    for j in range(i-K, i+K+1):
        # print(j)
        now_max += candy_list[j]
    # print('now',now_max)
    total_max = max(total_max, now_max)
print(total_max)
    

# 10 - 3 = 7
# 7-3, 7+3
# 8-3, 8+3
n = int(input())
arr = list(map(int, input().split()))

# 1등으로 큰 값부터 절반까지 뽑기
# 1등으로 작은 값부터 절반 까지 뽑기
# 1등으로 작은 값을 반대로 뒤집어서 위, 아래로 차를 구하기
# 이중 최솟값 뽑아서 출력

arr.sort()
total_nums = 2*n
bigs_half = arr[total_nums//2:]
smalls_half = arr[:total_nums//2]
# print(bigs_half, smalls_half)

val_min = 1000000
for i in range(n):
    diffs = bigs_half[i] - smalls_half[i]
    # print('diffs', diffs)
    val_min = min(diffs, val_min)
print(val_min)
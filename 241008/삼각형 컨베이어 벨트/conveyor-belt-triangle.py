n, t = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(3)]

# 모든 행은 오른쪽으로 밀리는 형태
# 모든 끝값을 저장해둬야 함
# 오른쪽으로 이동 후,
# 마지막 행값은 첫번째, 첫번째 행값은 두번째, 두번째 행값은 마지막 행으로 이동
# 이것을 t만큼 반복

for time in range(t):
    temp1 = nums[0][n-1]
    temp2 = nums[1][n-1]
    temp3 = nums[2][n-1]

    for i in range(n-1, 0, -1):
        nums[0][i] = nums[0][i-1]
        nums[1][i] = nums[1][i-1]
        nums[2][i] = nums[2][i-1]
    
    nums[0][0] = temp3
    nums[1][0] = temp1
    nums[2][0] = temp2

for elem in nums:
    for j in elem:
        print(j, end=" ")
    print()
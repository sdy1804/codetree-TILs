n, t = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(2)]

# 첫번째 행을 오른쪽 이동 시, 오른 맨 끝 숫자 사라지니 저장
# 두번째 행을 오른쪽 이동 시, 오른 맨 끝 숫자 사라지니 저장
# 오른쪽으로 이동 후, 각 저장한 숫자를 위치에 넣음
# 이를 t만큼 반복

for time in range(t):
    temp1 = nums[0][n-1]
    temp2 = nums[1][n-1]
    # print(temp1, temp2)

    for i in range(n-1, 0, -1): # 0, 1, 2
        nums[0][i] = nums[0][i-1] # nums[0][1] = nums[0][0]
        nums[1][i] = nums[1][i-1]
    # print(nums)
    nums[1][0] = temp1
    nums[0][0] = temp2

for elem in nums:
    for i in elem:
        print(i, end=" ")
    print(" ")
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 교차하는지 안하는지 확인하는 방법?
# 일단 x2 값에 따라 겹치는 여부가 정해지는듯
# 2개의 선분을 골라서, 해당 선분들의 값에 따라 케이스를 나눠 카운트하는 방법
# 선분1의 x1이 선분2의 x1보다 작을 때 -> 선분1의 x2가 선분2의 x2보다 작으면 겹치지 않음
# 선분1의 x1이 선분2의 x1보다 작을 때 -> 선분1의 x2가 선분2의 x2보다 크면 겹쳐짐
# 위 아래 반대 내용
# 선분1의 x1이 선분2의 x1보다 클 때 -> 선분1의 x2가 선분2의 x2보다 작으면 겹쳐짐
# 선분1의 x1이 선분2의 x1보다 클 때 -> 선분1의 x2가 선분2의 x2보다 크면 겹치지 않음

cnt = 0 
for i in range(N):
    for j in range(i+1, N):
        # print(arr[i], arr[j])
        l1_x1, l1_x2 = arr[i][0], arr[i][1]
        l2_x1, l2_x2 = arr[j][0], arr[j][1]
        if l1_x1 < l2_x1:
            if l1_x2 < l2_x2:
                cnt += 0
            else:
                cnt += 1
        else:
            if l1_x2 < l2_x2:
                cnt += 1
            else:
                cnt += 0
# print(cnt)
print(N - (cnt + 1))
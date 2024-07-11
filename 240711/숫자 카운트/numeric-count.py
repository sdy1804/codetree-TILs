N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 토론 참고 : A에 대한 크기 3인 1차원 배열 만들기
# 3중 for문으로 A의 값들 완전탐색
# 각 값들이 B에 있는지 확인
# 있다면, 위치가 같은지 다른지에 따라 해당 카운트를 조절
# 정보를 취합 후 조건이 맞으면 +1
# 각 자리를 정한다 -> B랑 값을 비교한다 -> (생각해야되는 조건) -> 카운트 증가 -> 카운트에 따른 값 출력
# 조건 = A의 각 자리수 마다 B에 들어가 있는지 없는지 확인
# 결국 카운트 변수 2개 써서 테케에 있는 값과 같으면 OK 아니면 PASS

cnt = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            
            succeeded = True
            for a, num_cnt1, num_cnt2 in arr:
                x = a // 100
                y = a // 10 % 10
                z = a % 10
                
                cnt1 = 0
                cnt2 = 0
                if x == i:
                    cnt1 += 1
                if y == j:
                    cnt1 += 1
                if z == k:
                    cnt1 += 1
                if x == j or x == k:
                    cnt2 += 1
                if y == i or y == k:
                    cnt2 += 1
                if z == i or z == j:
                    cnt2 += 1

                if cnt1 != num_cnt1 or cnt2 != num_cnt2:
                    succeeded = False
                    break
            if succeeded == True:
                cnt += 1
print(cnt)
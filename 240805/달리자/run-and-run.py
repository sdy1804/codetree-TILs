n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 부족한 곳이 생기면 가까운 곳에서부터 채워야 하는 방식?
# 줄어든 인원만큼 이동시켜야 함
# 2명을 뭉탱이로 움직여야 할지?
# 예제를 기준으로 생각해보기
# 인덱스 0: 2명이 줄어듦 -> 인덱스1로 이동가능? -> 줄어들었으므로 불가능 -> 줄어들지 않았으므로 인덱스2에 안착
# 인덱스 1: 2명이 줄어듦 -> 인덱스2로 이동가능? -> 현재 상태는 (5, 3)이므로 불가능 -> 인덱스3에 안착
# 인덱스 2: 2명이 줄어드는 상태로 변함 -> 인덱스 3으로 이동가능? -> 현재 상태는 (3, 5)이므로 가능 -> 인덱스 3에 안착
# A, B가 같아지면 종료? 아니면 for문을 n - 1까지만 반복
ans = 0
for idx in range(n-1):
    if B[idx] - A[idx] < 0:
        move_people = abs(B[idx] - A[idx])
        for i in range(idx+1, len(A)):
            if B[i] - A[i] >= 0:
                A[i] += abs(B[idx] - A[idx])
                A[idx] -= abs(B[idx] - A[idx])
                ans += move_people * abs(i - idx)
                break
print(ans)
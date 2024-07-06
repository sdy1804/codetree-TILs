N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 수열 B에 대한 순열을 구한 리스트를 만들고, -> OOM 및 시간복잡도 문제 발생
# A의 부분 수열의 모든 값이 B에 속하면 카운트 하는 방법
# 완전탐색으로 수열 A의 부분수열을 범위를 바꿔가며 만듦
# 범위에 의해 만들어진 A의 부분수열이 B에 속하면 cnt 증가

cnt = 0
for i in range(len(A)):
    for j in range(i, len(A)):
        part_A = A[i:j+1]
        if len(part_A) == len(B):
            cnt += 1 # 길이가 같은 부분집합 수를 카운트 해 놓음
            for k in range(len(part_A)): # 부분 집합을 돌면서
                if part_A[k] not in B: # B에 들어있지 않은 수가 나오면,
                    cnt -= 1 # 카운트 -1만 하고 탈출
                    break
print(cnt)
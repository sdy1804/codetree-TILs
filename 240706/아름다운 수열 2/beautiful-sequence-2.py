from itertools import permutations

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 수열 B에 대한 순열을 구한 리스트를 만들고,
# 완전탐색으로 수열 A의 부분수열을 범위를 바꿔가며 만듦
# 범위에 의해 만들어진 A의 부분수열이 B에 속하면 cnt 증가
B_list = []
for i in permutations(B):
    B_list.append(list(i))

cnt = 0
for i in range(len(A)):
    for j in range(i, len(A)):
        if A[i:j+1] in B_list:
            # print(A[i:j+1])
            cnt += 1
print(cnt)
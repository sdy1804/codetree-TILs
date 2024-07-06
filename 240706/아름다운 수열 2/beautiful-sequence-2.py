N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 수열 B에 대한 순열을 구한 리스트를 만들고, -> OOM 및 시간복잡도 문제 발생
# A의 부분수열이 B와 모든 값들에 포함되며, 중복된 값들의 개수에 대해서도 같아야 함
# 완전탐색으로 수열 A의 부분수열을 범위를 바꿔가며 만듦

cnt = 0
for i in range(len(A)):
    for j in range(i, len(A)):
        in_yes = False
        part_A = A[i:j+1]
        if len(part_A) == len(B):
            in_yes = True
            # print(part_A)
            for k in range(len(B)): 
                if (B[k] not in part_A) or (part_A[k] not in B) or (part_A.count(B[k]) != B.count(B[k])) or (part_A.count(part_A[k]) != B.count(part_A[k])):
                        # print('B[k]', B[k])
                        # print('part_A[k]',part_A[k])
                        in_yes = False
            # print(in_yes)   
        if in_yes:
            cnt += 1
print(cnt)
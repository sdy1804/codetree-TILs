import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 끝 돌은 포함하지 않음
# 최대값을 1부터 arr의 max값일 때까지 탐색 -> 최대값이 arr의 첫번째 또는 마지막 값일 때 예외처리 필요
# 각 최대값의 경우에서 최대값보다 작은 값들의 인덱스를 뜯어냄
# 인덱스 간의 거리계산을 통해 k보다 작거나 같게 끝까지 돌면 OK
# True인 경우에서 ans값을 갱신하여 최소값 찾기

def find_case(a):
    temp_list = []
    now_max = 0
    for i, elem in enumerate(arr):
        if elem <= a or i == 0 or i == (len(arr)-1):
            temp_list.append(i)
    # print(temp_list)
    if len(temp_list) == 1:
        return False, None
    for j in range(1, len(temp_list)):
        dist = temp_list[j] - temp_list[j-1]
        if dist > k:
            return False, None
    for i in range(len(temp_list)):
        now_max = max(now_max, arr[temp_list[i]])
    # print('now_max', now_max)
    return True, now_max

# print(find_case(1))
total_max_min = sys.maxsize
for i in range(1, max(arr)+1):
    bl, max_val = find_case(i)
    if bl:
        total_max_min = min(total_max_min, max_val)
print(total_max_min)
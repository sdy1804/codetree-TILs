import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# 처음부터 끝 - T까지를 첫 탐색 지점으로 설정
# 시작저부터 T만큼의 구간에서 각 포인트별로 드는 비용을 계산
# 계속 min 값을 갱신

total_min = sys.maxsize
for i in range(len(arr) - T + 1):
    now_min = 0
    for j in range(i, i + T):
        now_min += abs(H - arr[j])
    total_min = min(now_min, total_min)
print(total_min)
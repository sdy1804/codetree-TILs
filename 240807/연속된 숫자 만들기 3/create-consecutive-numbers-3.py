arr = list(map(int, input().split()))

# 1. 수 간격이 더 큰 쪽을 두고, 작은 쪽을 움직이기
# 2. 두 간격이 같은 경우는 어느 쪽을 움직여도 마찬가지
# 최종적인 이동횟수는 큰 쪽 간격 - 1

if abs(arr[0] - arr[1]) > abs(arr[1] - arr[2]):
    print(abs(arr[0] - arr[1]) - 1)
elif abs(arr[0] - arr[1]) < abs(arr[1] - arr[2]):
    print(abs(arr[1] - arr[2]) - 1)
else:
    print(abs(arr[0] - arr[1]) - 1)
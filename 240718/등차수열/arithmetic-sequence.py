n = int(input())
arr = list(map(int, input().split()))

# 완탐으로 k로 할 숫자 지정
# arr에서 숫자 2개를 골라 고른 2개의 숫자의 대소관계를 if문으로 확인
# 두개의 숫자와 각 차이 값을 계산해 같으면 카운트
total_max = 0
for k in range(min(arr), max(arr)):
    now_max = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j] and i < j:
                if arr[i] - k == k - arr[j]:
                    now_max += 1
                    # print(arr[i], k, arr[j])
                    # print('차이값_1', arr[i] - k, k - arr[j])
            if arr[i] < arr[j] and i < j:
                if arr[j] - k == k - arr[i]:
                    now_max += 1
                    # print(arr[i], k, arr[j])
                    # print('차이값_2',arr[j] - k, k - arr[i])
    total_max = max(now_max, total_max)
print(total_max)
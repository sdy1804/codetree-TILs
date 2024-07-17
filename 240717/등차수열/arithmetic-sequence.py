n = int(input())
arr = list(map(int, input().split()))

# 완탐으로 k로 할 숫자 지정
# arr에서 숫자 2개를 골라 고른 2개의 숫자의 대소관계를 if문으로 확인
# 두개의 숫자와 각 차이 값을 계산해 같으면 카운트
cnt = 0
for k in range(min(arr), max(arr)):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                if arr[i] - k == k - arr[j]:
                    cnt += 1
                    # print(arr[i], k, arr[j])
                    # print('차이값_1', arr[i] - k, k - arr[j])
            if arr[i] < arr[j]:
                if arr[j] - k == k - arr[i]:
                    cnt += 1
                    # print(arr[j], k, arr[i])
                    # print('차이값_2',arr[j] - k, k - arr[i])
print(cnt)
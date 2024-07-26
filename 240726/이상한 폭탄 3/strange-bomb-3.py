N, K = map(int, input().split())
arr = list(int(input()) for _ in range(N))

# 폭탄을 하나씩 탐색하면서 +-K만큼 인덱스 안에 해당 정수가 있다면 카운트
# 인덱스가 없는 부분을 탐색할 시를 예외처리 해야함
# 폭탄의 Max값을 길이로 하는 리스트를 만들어 폭발횟수 기록
# 리스트에서 가장 큰 값의 인덱스를 출력

bomb_list = [0] * (max(arr)+1)

for i in range(N):
    for j in range(i-K, i+K+1):
        if j == i or j > N-1 or j < 0:
            continue
        # print('arr[i], arr[j])', arr[i], arr[j])
        if arr[i] == arr[j]:
            bomb_list[arr[i]] += 1
            break
    # print(bomb_list)
print(bomb_list.index(max(bomb_list)))
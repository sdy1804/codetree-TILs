N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(N):
    first = arr[i]
    # print('first', first)
    for j in range(i+1, N):
        if arr[j] > first:
            second = arr[j]
            # print('second', second)
            for k in range(j+1, N):
                if arr[k] > second:
                    cnt += 1
                    # print(cnt)
print(cnt)
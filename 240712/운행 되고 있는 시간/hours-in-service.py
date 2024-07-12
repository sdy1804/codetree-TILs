N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

total_max = 0
for i in range(N):
    work = []
    for j in range(N):
        if i == j:
            continue
        # print(arr[j])
        for k in range(arr[j][0], arr[j][1]):
            if k not in work:
                work.append(k)
    total_max = max(total_max, len(work))
print(total_max)
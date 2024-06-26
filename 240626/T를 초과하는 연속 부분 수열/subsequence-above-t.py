n, t = map(int, input().split())
arr = list(map(int, input().split()))

now_count, max_count = 0, 0
for i in range(n):
    if arr[i] > t:
        now_count += 1
        if now_count > max_count:
            max_count = now_count
    else:
        now_count = 0
    
print(max_count)
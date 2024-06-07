n = int(input())
arr = list(map(int, input().split()))
cnt = 0
min_val = arr[0]

for elem in arr[1:]:
    if elem < min_val:
        min_val = elem
print(min_val, end=" ")
for elem in arr:
    if elem == min_val:
        cnt += 1
print(cnt)
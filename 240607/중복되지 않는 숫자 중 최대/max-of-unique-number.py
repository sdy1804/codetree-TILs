n = int(input())
arr = list(map(int, input().split()))
new_arr = []

for elem in arr:
    if arr.count(elem) == 1:
        new_arr.append(elem)
if new_arr:
    print(max(new_arr))
else:
    print(-1)
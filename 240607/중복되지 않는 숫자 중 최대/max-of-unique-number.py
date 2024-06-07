n = int(input())
arr = list(map(int, input().split()))
check = False
max_val = arr[0]

for elem in arr[1:]:
    if max_val < elem:
        max_val = elem
    elif max_val == elem:
        check = True
if check == True:
    print(-1)
else:
    print(max_val)
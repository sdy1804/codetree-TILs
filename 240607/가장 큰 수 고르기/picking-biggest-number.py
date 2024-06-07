arr = list(map(int, input().split()))

max_val = arr[0]

for elem in arr[1:]:
    if elem > max_val:
        max_val = elem
print(max_val)
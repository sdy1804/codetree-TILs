arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        arr = arr[:i]
        break

new_arr = [elem+3 if elem % 2 != 0 else elem//2 for elem in arr]

for i in new_arr:
    print(i, end=" ")
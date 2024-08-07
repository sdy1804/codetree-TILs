n = int(input())
arr = list(input().split())

# bubblesort 방식
# A D C B -> A C D B -> A C B D -> A B C D

sorted_arr = sorted(arr)

cnt = 0
while sorted_arr != arr:
    for i in range(n - 1):
        if ord(arr[i]) > ord(arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            cnt += 1
print(cnt)
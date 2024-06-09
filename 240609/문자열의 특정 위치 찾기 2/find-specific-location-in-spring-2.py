string = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]
ans = []
cnt = 0

for i in range(len(arr)):
    if arr[i][2] == string or arr[i][3] == string:
        print(arr[i])
        cnt += 1
print(cnt)
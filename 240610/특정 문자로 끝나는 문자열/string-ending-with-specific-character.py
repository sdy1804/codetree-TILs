arr = [input() for _ in range(10)]
alpha = input()

for i in range(len(arr)):
    if arr[i][-1] == alpha:
        print(arr[i])
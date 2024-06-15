n = input()
arr = []
for i in range(len(n)):
    arr.append(int(n[i]))

num = 0
for j in range(len(arr)):
    num = num * 2 + arr[j]
print(num)
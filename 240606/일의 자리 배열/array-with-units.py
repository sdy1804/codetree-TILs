first, second = map(int, input().split())
arr = []
arr.append(first)
arr.append(second)
for i in range(3, 11):
    arr.append(arr[-1] + arr[-2])

new_arr = [i % 10 for i in arr]

for elem in new_arr:
    print(elem, end=" ")
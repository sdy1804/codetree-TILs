n = int(input())
arr = list(map(int, input().split()))

new_arr = [elem**2 for elem in arr]

for i in new_arr:
    print(i, end= " ")
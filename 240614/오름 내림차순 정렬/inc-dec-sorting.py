n = int(input())
arr = list(map(int, input().split()))

sort_arr = sorted(arr)
reverse_arr = sort_arr[::-1]

for elem in sort_arr:
    print(elem, end=" ")
print()
for elem in reverse_arr:
    print(elem, end=" ")
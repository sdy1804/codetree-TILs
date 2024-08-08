n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

first_leng = abs(arr[0][0] - arr[-2][1])
# print(first_leng)
second_leng = abs(arr[1][0] - arr[-1][1])
# print(second_leng)

if first_leng < second_leng:
    print(first_leng)
else:
    print(second_leng)
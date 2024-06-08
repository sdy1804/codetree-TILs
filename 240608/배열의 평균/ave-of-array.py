arr_2d = [list(map(int, input().split())) for i in range(2)]
total_sum = 0

for i in range(2):
    sum_row = sum(arr_2d[i])
    avg_row = sum_row / len(arr_2d[i])
    print(f"{avg_row:.1f}", end=" ")
print()

for j in range(4):
    sum_column = arr_2d[0][j] + arr_2d[1][j]
    avg_column = sum_column / 2
    print(f"{avg_column:.1f}", end=" ")
print()

for i in range(2):
    total_sum += sum(arr_2d[i])
total_avg = total_sum / 8
print(f"{total_avg:.1f}", end=" ")
print()
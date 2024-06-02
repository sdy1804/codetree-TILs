n = int(input())
sum, avg, length = 0, 0, 0

for i in range(n):
    num = int(input())
    sum += num
    length += 1
avg = sum / length
print(sum, f"{avg:.1f}")
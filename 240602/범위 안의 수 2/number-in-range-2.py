sum, avg, length = 0, 0, 0

for i in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        sum += n
        length += 1
avg = sum / length

print(sum, f"{avg:.1f}")
a, b = map(int, input().split())
sum, avg = 0, 0
length = 0

for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        sum += i
        length += 1
avg = sum / length
print(sum, f"{avg:.1f}")
arr = list(map(int, input().split()))
sum = 0
length = 0

for elem in arr:
    if elem >= 250:
        break
    else:
        sum += elem
        length += 1
avg = sum / length
print(sum, f"{avg:.1f}")
A, B, C = map(int, input().split())

total_max = 0
for i in range(1000):
    for j in range(1000):
        now_max = A * i + B * j
        if now_max <= C:
            total_max = max(now_max, total_max)
print(total_max)
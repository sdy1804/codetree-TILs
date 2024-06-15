m1, d1, m2, d2 = map(int, input().split())
elapsed_days1, elapsed_days2 = 0, 0
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for d in range(m1):
    elapsed_days1 += days[d]
elapsed_days1 += d1
# print(elapsed_days1)

for d in range(m2):
    elapsed_days2 += days[d]
elapsed_days2 += d2
# print(elapsed_days2)

print(elapsed_days2 - elapsed_days1+1)
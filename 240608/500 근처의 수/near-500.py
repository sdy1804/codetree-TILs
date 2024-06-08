arr = list(map(int, input().split()))
max_val = 0
min_val = 1000

for elem in arr:
    if elem < 500 and elem > max_val:
        max_val = elem
    if elem > 500 and elem < min_val:
        min_val = elem
print(max_val, min_val)
a = list(input())
for i in range(len(a)):
    a[i] = int(a[i])

max_val = 0

def two_to_ten(arr):
    num = 0
    for i in range(len(arr)):
        num = num * 2 + arr[i]
    return num

for i in range(len(a)):
    if a[i] == 1:
        a[i] = 0
        max_val = max(max_val, two_to_ten(a))
        a[i] = 1
    elif a[i] == 0:
        a[i] = 1
        max_val = max(max_val, two_to_ten(a))
        a[i] = 0
print(max_val)
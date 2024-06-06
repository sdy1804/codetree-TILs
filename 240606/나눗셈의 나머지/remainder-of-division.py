a, b = map(int, input().split())
left = [0]*10
sum = 0

while 1:
    if a <= 1:
        break
    else:
        remain = a % b
        left[remain] += 1
        a = a // b
for i in left:
    sum += i**2
print(sum)
n = int(input())
arr = []

arr.append(1)
arr.append(n)

while 1:
    elem = arr[-2] + arr[-1]
    arr.append(elem)
    if elem > 100:
        break

for i in arr:
    print(i, end=" ")
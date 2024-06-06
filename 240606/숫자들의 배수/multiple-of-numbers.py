n = int(input())
arr =[]
cnt = 0
mult = 1

while 1:
    elem = n * mult
    arr.append(elem)
    mult += 1
    if elem % 5 == 0:
        cnt += 1
        if cnt == 2:
            break
for i in arr:
    print(i, end=" ")
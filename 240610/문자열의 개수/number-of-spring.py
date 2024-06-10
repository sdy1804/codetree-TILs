cnt = 0
arr = []

for i in range(200):
    string = input()
    if string == '0':
        print(cnt)
        break
    else:
        cnt += 1
        if i % 2 == 0:
            arr.append(string)

for elem in arr:
    print(elem)
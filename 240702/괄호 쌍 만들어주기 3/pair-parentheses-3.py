string = input()

cnt = 0
for i in range(len(string)):
    if string[i] == '(':
        for j in range(i+1, len(string)):
            if string[j] == ')':
                cnt += 1
print(cnt)
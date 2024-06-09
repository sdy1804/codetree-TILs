string = input()
lowercase = input()
cnt = 0

for i in string:
    if i == lowercase:
        cnt += 1
print(cnt)
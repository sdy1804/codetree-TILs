string = input()
ans = []

for i in range(len(string)):
    if i % 2 != 0:
        ans.append(string[i])

for elem in ans[::-1]:
    print(elem, end="")
s, q = input().split()
s = list(s)
q = int(q)
questions = list(input().split() for _ in range(q))
for j in range(len(questions)):
    if questions[j][0] == '1':
        for k in range(len(questions[j])):
            questions[j][k] = int(questions[j][k])
# print(questions)

for arr in questions:
    # print(type(arr[0]))
    if arr[0] == 1:
        s[arr[1]-1], s[arr[2]-1] = s[arr[2]-1], s[arr[1]-1]
        for elem in s:
            print(elem, end="")
        print()
    else:
        for i in range(len(s)):
            if s[i] == arr[1]:
                s[i] = arr[2]
        for elem in s:
            print(elem, end="")
        print()
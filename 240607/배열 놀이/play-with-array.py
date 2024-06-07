n, q = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(q):
    questions = list(map(int, input().split()))
    if questions[0] == 1:
        print(arr[questions[1] - 1])
    elif questions[0] == 2:
        if questions[1] in arr:
            print(arr.index(questions[1]) + 1)
        else:
            print(0)
    elif questions[0] == 3:
        for i in range(questions[1] - 1, questions[2]):
            print(arr[i], end=" ")
        print()
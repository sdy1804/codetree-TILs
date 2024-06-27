N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(M)]

students = [i for i in range(1, N+1)]
penalties = [0 for _ in range(len(students))]

penalty = False
for num in arr:
    penalties[num-1] += 1
    if 3 in penalties:
        print(penalties.index(3) + 1)
        penalty = True
        break

if penalty == False:
    print(-1)
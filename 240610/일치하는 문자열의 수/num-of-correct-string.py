n, string = input().split()
n = int(n)
cnt = 0

for i in range(n):
    compare = input()
    if compare == string:
        cnt += 1
print(cnt)
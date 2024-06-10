a, b = map(int, input().split())
sum = a + b
cnt = 0

for s in str(sum):
    if s == '1':
        cnt += 1
print(cnt)
n = int(input())
sum = 0

for i in range(n):
    num = int(input())
    sum += num

sum = str(sum)
print(sum[1:]+sum[0])
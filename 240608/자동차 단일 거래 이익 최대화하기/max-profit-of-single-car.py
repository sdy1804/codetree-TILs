n = int(input())
arr = list(map(int, input().split()))

max_profit = 0

for i in range(n):
    for j in range(i+1, n):
        profit = arr[j] - arr[i]
        if profit > max_profit:
            max_profit = profit
print(max_profit)
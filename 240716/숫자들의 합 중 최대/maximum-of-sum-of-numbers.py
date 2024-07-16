X, Y = map(int, input().split())

total_max = 0
for i in range(X, Y+1):
    ten_thousand = i // 10000
    thousand = i //1000 % 10
    hundred = i // 100 % 10
    ten = i // 10 % 10
    one = i % 10
    now_max = ten_thousand + thousand + hundred + ten + one
    total_max = max(now_max, total_max)
    # print(ten_thousand)
    # print(thousand)
    # print(hundred)
    # print(ten)
    # print(one)
print(total_max)
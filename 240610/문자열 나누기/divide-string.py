n = int(input())
arr = list(map(str, input().split()))
str_all = ""
ans = []

for i in arr:
    str_all += i

for j in range(0, len(str_all), 5):
    ans.append(str_all[j:j+5])

for elem in ans:
    print(elem)
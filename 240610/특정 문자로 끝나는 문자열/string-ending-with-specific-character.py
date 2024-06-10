arr = [input() for _ in range(10)]
alpha = input()
exist = False

for i in range(len(arr)):
    if arr[i][-1] == alpha:
        print(arr[i])
        exist =True
if exist == False:
    print('None')
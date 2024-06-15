a, b = map(int, input().split())
n = list(map(int, list(input())))

def change_to_ten(arr, change):
    num = 0
    for i in range(len(arr)):
        num = num * change + arr[i]
    return num

def change_to_other(n, change):
    arr = []
    while 1:
        if n < change:
            arr.append(n % change)
            break
        arr.append(n % change)
        n //= change
    return arr

new_ten = change_to_ten(n, a)
for elem in change_to_other(new_ten, b)[::-1]:
    print(elem, end="")
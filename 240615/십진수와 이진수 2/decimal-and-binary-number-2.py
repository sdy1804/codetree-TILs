N = list(map(int, list(input())))

def change_to_ten(arr):
    num = 0
    for i in range(len(arr)):
        num = num * 2 + arr[i]
    
    return num
# print(change_to_ten(N))

new_N = change_to_ten(N) * 17

def change_to_binary(n):
    arr = []
    while 1:
        if n < 2:
            arr.append(n % 2)
            break
        arr.append(n % 2)
        n //= 2
    return arr

for elem in change_to_binary(new_N)[::-1]:
    print(elem, end="")
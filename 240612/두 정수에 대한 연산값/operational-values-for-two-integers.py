def change_val(A, B):
    if A > B:
        A += 25
        B *= 2
    else:
        B += 25
        A *= 2
    return A, B

a, b = map(int, input().split())
a, b = change_val(a, b)
print(a, b)
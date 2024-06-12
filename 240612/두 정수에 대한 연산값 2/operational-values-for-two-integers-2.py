def change_val(A, B):
    if A > B:
        B += 10
        A *= 2
    else:
        A += 10
        B *= 2
    return A, B

a, b = map(int, input().split())
a, b = change_val(a, b)
print(a, b)
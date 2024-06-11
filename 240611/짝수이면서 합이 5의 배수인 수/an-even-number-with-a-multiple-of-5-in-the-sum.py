def is_even_five(n):
    n = str(n)
    ten = int(n[0])
    one = int(n[1])
    if (ten + one) % 5 == 0 and int(n) % 2 == 0:
        print("Yes")
    else:
        print("No")

n = int(input())
is_even_five(n)
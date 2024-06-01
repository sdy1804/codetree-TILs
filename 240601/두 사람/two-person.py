A_age, A_sex = input().split()
B_age, B_sex = input().split()

A_age, B_age = int(A_age), int(B_age)

if (A_age >= 19 and A_sex == 'M') or (B_age >= 19 and B_sex == 'M'):
    print(1)
else:
    print(0)
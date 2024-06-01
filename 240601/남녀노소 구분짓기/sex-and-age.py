sex = int(input())
age = int(input())

if age >= 19:
    if sex == 0:
        print("MAN")
    else:
        print("WOMAN")
else:
    if sex == 0:
        print("BOY")
    else:
        print("GIRL")
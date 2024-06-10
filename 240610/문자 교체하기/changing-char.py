str_1, str_2 = input().split()

str_1 = list(str_1)
str_2 = list(str_2)

str_2[0], str_2[1] = str_1[0], str_1[1]

for elem in str_2:
    print(elem, end="")
string_1, string_2 = input().split()

if len(string_1) > len(string_2):
    print(string_1, len(string_1))
elif len(string_1) == len(string_2):
    print('same')
else:
    print(string_2, len(string_2))